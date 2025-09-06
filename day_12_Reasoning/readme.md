# Hands-On Activity: Exploring Reasoning with Ollama

## Step-by-Step Instructions

### Step 1: Download and Setup Ollama
- Ensure you have Ollama installed on your system. If not, download it from [Ollama's official website](https://ollama.com/download).

### Step 2: Run the Model
- Open your terminal and execute the following command to run the deepseek-r1:8b model:
  ```bash
  ollama run deepseek-r1:8b
  ```

### Step 3: Test and Explore the Thinking Model
- Engage with the model using the following prompts. Try to understand the reasoning process behind each response.

#### Simple Prompts
- What is the capital of France?
- Who is Jose Rizal?

#### Mathematical Reasoning
- A farmer has chickens and rabbits. Together they have 35 heads and 94 legs. How many chickens and how many rabbits does the farmer have? Show your step-by-step reasoning.
- If you fold a piece of paper in half 7 times, how thick will it be compared to the original thickness? Explain your reasoning process.
- Three friends split a restaurant bill. Alex pays 40% of the total, Beth pays $15 more than Chris, and Chris pays $25. What was the total bill?

#### Logic Puzzles
- You have 12 balls that look identical. 11 weigh exactly the same, but one is either heavier or lighter. Using a balance scale only 3 times, how can you identify the odd ball and determine if it's heavier or lighter?
- Five people live in five houses of different colors, drink different beverages, smoke different brands, and keep different pets. Using these clues, determine who owns the fish: [Then provide a classic logic grid puzzle]

#### Strategic Reasoning
- You're playing a game where you and an opponent take turns removing 1, 2, or 3 stones from a pile of 21 stones. The person who takes the last stone wins. You go first. What's your winning strategy?
- Two companies are bidding for a contract. If you bid too high, you lose. If you bid too low, you win but make little profit. The contract is worth $100M to you, but you don't know its value to your competitor. How do you decide what to bid?

#### Analytical Reasoning
- A company's profits increased by 25% in Year 1, decreased by 20% in Year 2, and increased by 10% in Year 3. If they started with $1M profit, what's their profit now and what was their average annual growth rate?
- Explain why correlation doesn't imply causation using a specific example, then describe three methods researchers use to establish causal relationships.

#### Creative Problem Solving
- You need to measure exactly 4 liters of water, but you only have a 3-liter jug and a 5-liter jug. Neither has measurement marks. How do you do it?
- Design a fair system for 100 people to split into teams when some people refuse to work with others. What principles would you use and what's your step-by-step process?

#### Multi-step Reasoning
- A train travels from City A to City B at 60 mph, then from City B to City C at 80 mph. The total distance is 280 miles and the total time is 4 hours. Find the distance between each pair of cities. Show all your work.
- If today is Wednesday and it was Monday 100 days ago, what day of the week will it be 50 days from now? Explain your reasoning method.

#### Ethical Reasoning
- A self-driving car's AI must choose between hitting one person or swerving to hit three people. How should it decide? Consider multiple ethical frameworks in your analysis.
- Should a doctor prescribe a placebo if they know it will help the patient psychologically but involves deception? Analyze this from different ethical perspectives.

## Reflection Questions
- What are your key observations from the thinking process?
- Were there any "Aha" moments for you?
- Did you notice any inefficiencies or mistakes in the thinking process?
- How could you improve the reasoning process?

## Part 2: Fine-Tuning with Reasoning Data (Optional)

This notebook is best run on an A100... takes ages to complete on a T4.
If you truly want to learn fine-tuning, invest in compute.

- Explore how to fine-tune Qwen with reasoning data using this [notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(14B)-Reasoning-Conversational.ipynb#scrollTo=kR3gIAX-SM2q).