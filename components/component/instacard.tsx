/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/KxNhZ4zRjTR
 */
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { CardTitle, CardDescription, CardHeader, CardContent, Card } from "@/components/ui/card"

export function Instacard() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-black">
      <div className="w-full max-w-md p-4 space-y-6">
        <h2 className="text-center text-3xl font-extrabold text-gray-100">Instagram Hashtag Generator</h2>
        <div className="grid w-full gap-1.5">
          <Label className="text-gray-100" htmlFor="image-upload">
            Upload an Image
          </Label>
          <Input id="image-upload" type="file" />
        </div>
        <Card className="w-full bg-gray-00 text-gray-100">
          <CardHeader>
            <CardTitle>Generated Hashtags</CardTitle>
            <CardDescription>Here are the hashtags generated based on your image.</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid gap-2">
              <div className="flex items-center justify-between">
                <span className="font-medium">#1</span>
                <span className="text-gray-500">#beachlife</span>
                <span className="text-gray-400">Videos: 1.2M</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-medium">#2</span>
                <span className="text-gray-500">#sunset</span>
                <span className="text-gray-400">Videos: 900K</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-medium">#3</span>
                <span className="text-gray-500">#travel</span>
                <span className="text-gray-400">Videos: 2.3M</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-medium">#4</span>
                <span className="text-gray-500">#nature</span>
                <span className="text-gray-400">Videos: 1.8M</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="font-medium">#5</span>
                <span className="text-gray-500">#photography</span>
                <span className="text-gray-400">Videos: 2.1M</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
