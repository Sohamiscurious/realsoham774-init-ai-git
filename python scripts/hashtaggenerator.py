import os
import json
import re
from googleapiclient.discovery import build
import google.generativeai as genai

# Your API key for YouTube Data API
youtube_api_key = "AIzaSyDw2BPo7POvFNI95DrA_MumAE84PLfr98k"

# Your API key for Generative AI
generative_ai_api_key = "AIzaSyDwBqn8tMERvG964BA9wggcGMtx5-IT_Io"

# Function to fetch YouTube data for a list of keywords
def fetch_youtube_data(keywords):
    all_hashtags = []
    for keyword in keywords:
      #  print(f"Fetching data for keyword: {keyword}")
        # Build the YouTube Data API service object
        youtube = build("youtube", "v3", developerKey=youtube_api_key)

        # Define the search request parameters
        search_request = youtube.search().list(
            part="snippet",
            q=keyword,
            maxResults=25,
            type="VIDEO"
        )

        try:
            # Execute the search request
            search_response = search_request.execute()

            # Extract video data and create a list of video IDs
            video_ids = [item["id"]["videoId"] for item in search_response["items"]]

            # Fetch details for each video using the videos endpoint
            videos = []
            for video_id in video_ids:
                video_request = youtube.videos().list(
                    part="snippet,statistics",  # Include snippet and statistics only
                    id=video_id
                )
                video_response = video_request.execute()
                video_data = video_response["items"][0]
                
                # Extract relevant information
                video_info = {
                    "title": video_data["snippet"]["title"],
                    "description": video_data["snippet"]["description"],
                    "views": video_data["statistics"]["viewCount"],
                    "likes": video_data["statistics"].get("likeCount", 0),  # Check if likeCount exists, default to 0
                }
                videos.append(video_info)

            # Sort videos by views count
            sorted_videos = sorted(videos, key=lambda x: x["views"], reverse=True)

            # Save the sorted data as a JSON file
            file_name = f"youtube_data_sorted_{keyword}.json"
            with open(file_name, "w") as f:
                json.dump(sorted_videos, f, indent=4)

         #   print(f"Sorted YouTube data for {keyword} saved to {file_name}")

            # Extract hashtags from the sorted JSON file
            hashtags_list = []
            for video in sorted_videos:
                description = video.get("description", "")
                # Extract hashtags using regular expression
                hashtags = re.findall(r'#\w+', description)
                hashtags_list.extend(hashtags)
                all_hashtags.extend(hashtags)

            if hashtags_list:
                pass
               # print(f"Extracted hashtags for {keyword}:", hashtags_list)
            else:
                pass
               # print(f"No hashtags found for {keyword}.")

        except Exception as e:
            pass
            #print(f"An error occurred for {keyword}: {e}")

    return all_hashtags

# Function to get response from Generative AI
def get_gemini_response(hashtags_list, my_string):
    genai.configure(api_key=generative_ai_api_key)
    model = genai.GenerativeModel("gemini-pro")
    concatenated_string = ''.join(hashtags_list) + my_string
    response = model.generate_content(concatenated_string) 
    return response.text

# Main function
def main():
    # Fetch YouTube data
    keyword_list = ["Narendra modi","ElonMusk","Tesla"]  # Example usage with a list of keywords
    hashtags_list = fetch_youtube_data(keyword_list)

    # Generate response using Generative AI
    my_string = "Create a set of concise and relevant hashtags for your content, ensuring minimal redundancy while effectively capturing key themes. Consider the target audience and aim for a balance between specificity and popularity in hashtag:"
    print(get_gemini_response(hashtags_list, my_string))

if __name__ == "__main__":
    main()
