import { useState } from "react";
import { Zap, Target, Code, Clock, Users } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Label } from "@/components/ui/label";

export const ExerciseGenerator = () => {
  const [difficulty, setDifficulty] = useState("");
  const [topic, setTopic] = useState("");
  const [generatedExercise, setGeneratedExercise] = useState(null);
  const [isGenerating, setIsGenerating] = useState(false);

  const generateExercise = async () => {
    setIsGenerating(true);
    
    // Simulate AI exercise generation
    setTimeout(() => {
      const exercises = {
        "beginner-arrays": {
          title: "Sum of Array Elements",
          description: "Write a function that calculates the sum of all elements in an array of numbers.",
          difficulty: "Beginner",
          estimatedTime: "15 min",
          hints: [
            "Use a loop to iterate through the array",
            "Keep a running total as you iterate",
            "Don't forget to return the total"
          ],
          starterCode: `function sumArray(numbers) {
  // Your code here
  
}

// Test cases
console.log(sumArray([1, 2, 3, 4])); // Expected: 10
console.log(sumArray([10, -2, 5])); // Expected: 13`,
          solution: `function sumArray(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}`,
          topics: ["Arrays", "Loops", "Basic Algorithms"]
        },
        "intermediate-recursion": {
          title: "Factorial Calculator",
          description: "Implement a recursive function to calculate the factorial of a given number.",
          difficulty: "Intermediate",
          estimatedTime: "25 min",
          hints: [
            "Remember the base case: factorial of 0 or 1 is 1",
            "Use recursive calls for n > 1",
            "factorial(n) = n * factorial(n-1)"
          ],
          starterCode: `function factorial(n) {
  // Your code here
  
}

// Test cases
console.log(factorial(5)); // Expected: 120
console.log(factorial(0)); // Expected: 1`,
          solution: `function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}`,
          topics: ["Recursion", "Mathematical Functions", "Base Cases"]
        }
      };

      const key = `${difficulty}-${topic}`;
      const exercise = exercises[key] || exercises["beginner-arrays"];
      
      setGeneratedExercise(exercise);
      setIsGenerating(false);
    }, 2000);
  };

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Zap className="h-5 w-5" />
            <span>AI Exercise Generator</span>
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="difficulty">Difficulty Level</Label>
              <Select value={difficulty} onValueChange={setDifficulty}>
                <SelectTrigger>
                  <SelectValue placeholder="Select difficulty" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="beginner">Beginner</SelectItem>
                  <SelectItem value="intermediate">Intermediate</SelectItem>
                  <SelectItem value="advanced">Advanced</SelectItem>
                </SelectContent>
              </Select>
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="topic">Topic</Label>
              <Select value={topic} onValueChange={setTopic}>
                <SelectTrigger>
                  <SelectValue placeholder="Select topic" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="arrays">Arrays</SelectItem>
                  <SelectItem value="recursion">Recursion</SelectItem>
                  <SelectItem value="sorting">Sorting</SelectItem>
                  <SelectItem value="strings">Strings</SelectItem>
                  <SelectItem value="objects">Objects</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          <Button 
            onClick={generateExercise} 
            disabled={!difficulty || !topic || isGenerating}
            className="w-full"
          >
            <Zap className="h-4 w-4 mr-2" />
            {isGenerating ? "Generating Exercise..." : "Generate AI Exercise"}
          </Button>
        </CardContent>
      </Card>

      {generatedExercise && (
        <Card>
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle className="text-lg">{generatedExercise.title}</CardTitle>
              <div className="flex items-center space-x-2">
                <Badge variant="outline">{generatedExercise.difficulty}</Badge>
                <Badge variant="secondary">
                  <Clock className="h-3 w-3 mr-1" />
                  {generatedExercise.estimatedTime}
                </Badge>
              </div>
            </div>
          </CardHeader>
          <CardContent className="space-y-4">
            <p className="text-muted-foreground">{generatedExercise.description}</p>
            
            <div className="space-y-3">
              <h4 className="font-medium flex items-center space-x-2">
                <Target className="h-4 w-4" />
                <span>Hints</span>
              </h4>
              <ul className="space-y-2">
                {generatedExercise.hints.map((hint, index) => (
                  <li key={index} className="flex items-start space-x-2 text-sm">
                    <span className="text-primary">•</span>
                    <span>{hint}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="space-y-3">
              <h4 className="font-medium flex items-center space-x-2">
                <Code className="h-4 w-4" />
                <span>Starter Code</span>
              </h4>
              <div className="bg-code-bg text-code-foreground p-4 rounded-md font-mono text-sm overflow-x-auto">
                <pre>{generatedExercise.starterCode}</pre>
              </div>
            </div>

            <div className="flex flex-wrap gap-2">
              {generatedExercise.topics.map((topic, index) => (
                <Badge key={index} variant="outline" className="text-xs">
                  {topic}
                </Badge>
              ))}
            </div>

            <div className="flex space-x-2">
              <Button className="flex-1">
                <Target className="h-4 w-4 mr-2" />
                Start Exercise
              </Button>
              <Button variant="outline">
                View Solution
              </Button>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};