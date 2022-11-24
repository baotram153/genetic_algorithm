# GENETIC ALGORITHM OVERVIEW
## 1. What is Genetic Algorithm?
- the concept of Genetic Algorithm
	- stochastic global optimization algorithm inspired by evolution by means of natural selection
	- this 'natural selection' process in evolutionary computing is a metaphor for a particular style of problem solving - that of trials and errors
- some biology terminology
	- 'survival of the fittest'
	- Wright's 'adaptive landscape', 'shifting balance theory', 'multimodel', 'unimodel', 'local maxima', 'global maximum'
	- 'genotype', 'phenotype', 'pleitropy' (one gene affect more phenotype traits), 'polygeny' (one phenotype being affected by more genes) , 'genome', 'diploid', 'haploid', 'gamete', 'zygote'
- generate-and-test method
- when consider nature as a problem solver, 2 candidates are considered:
	- the human brain $\rightarrow$ neurocomputing
	- the evolutionary process  $\rightarrow$ evolutionary computing
- why?
	- the power of natural evolution is evident in the diverse and harmonious world that we are living in, where each species are tailored to survive well in its own niche
	- the need for solving a large number of problems with more and more complexity in restricted time
	- evolutionary computing provides the possibility of conducting experiments different from traditional biology. with computer millions of generations can be generated within the matter of hours or days
- the main function of the algorithm is looping through those processes over and over until there are no further improvements in a number of the latest best solutions
- the iteration is an effort of mimicking natural selection
	- first, each candidate solution is evaluated using an objective function. the objective function evaluation is understood as the fitness of that candidate solution
	- find pairs of parents with high(est) fitness points to reproduce the next generation which has a high probability of having high fitness point inherited from their parents. one effective way to do that is fetching random k solution candidates and choose the fittest to be a parent (this is called tournament selection with a hyperparameter of k set to a certain number)
	- parents are then taken in pairs as an effort to create a new generation. first we recombine the "gene" of two parents using crossover operator.
	- in crossover operator, we choose a random split point, the child is then created by combine the bits from the start of the bitstring to the split point of the first parent and from the split point to the end of the bitstring of the second.
	- crossover is applied probabilistically and is often controlled by a hyperparameter set to a large number such as 80 or 90 percent.
	- if we only use crossover as the tool for optimization but the size of the population is too small, it's easier for us to reach the point when children's generation is exactly akin to their parents' and no further improvements are made. to avoid this, we use another method call mutation, in which we randomly select a bit from the bitstring and flip it. mutation rate is also set by a hyperparameter is often pretty low (about 1/L when L is the length of the bitstring)
		- this is understandable because if the mutation rate is too high, we will then return to a situation similar to Brute Force Search where everything appears randomly


## 2. Problems use Genetic Algorithm
- Example problems
	- Find a goal string
	- The Onemax problem
	- The Knapsack problem
	- The Traveling Saleman
	- Compare with Brute Force Search 
### Types of problems that are commonly associated with Artificial Intelligent
1. Optimization, Modelling and Simulation problems
- problems in this category is based on a Black box model of computer system
    - Optimization problems
        - have the model for calculating the the fitness (or the rightness) of the solution, and the expecting output (the desired output is decided implicitly (The Saleman Problem) or explicitly (The Eight-Queen Problem)), the task is to find the inputs that lead to that output

    - Modelling problems
        - have a set of inputs and their desired outputs, the task is to find a model that is able deliver the correct output to each known input
            - e.g: 
	            - the task of identifying the traffic signs from images
		            - preprocessing stage: each image is divided into regions of interests (that might be a traffic light), then for each one they produce a numerical description of relevant features such as brightness, contrast, colors, size, shape...
		            - main process: inputs are taken as vectors of numbers and outputs are the responding predefined labels
	            - voice controll system for smart homes
        - can also be convert into Optimization problems: e.g: we have a wide range of models and want to know which model produce the most satisfactory outputs

    - Simulation problems
        - know the system model and the inputs, need to compute the outputs corresponding to these inputs
        - e.g: 
	        - eletrical circuit where we have some inputs and the model that contains the rules of how circuit components work, we have to find the ouput corresponding to our given inputs
	        - in finance where we are given data about the current market and economic situation and we need to find the appropriate investment strategy
        - advantages: test out things with little budget or is impossible to be carried out in real world

2. Search problems
    - it can be inferred from the black box view of the system that the computational process is directional: from input towards output and cannot be inverted. 
    - in simulation problem, we could simply give the model a set of inputs and wait for the corresponding output, but we cannot do the same for optimization and modelling problems. the task of finding a satisfactory input or model require the identification of a particular object in the sea of various possibilities. this is why those problems that are solved this way are called 'search problems'
    - steps to defining a search problem
        - specification of a search space
            - all possible inputs of our model (optimization problems)
            - all possible computational models that describe the relationship between our two set of inputs and outputs (modelling problems)
        - definition of a solution (implicitly or explicitly)
3. Optimization vs. Constraint Satisfaction
    - an objective function assign a value of a possible solution that reflects its quality on a scale
    - a constraint is a binary value of 'yes' and 'no' that will tell if a solution holds or not
    - a solution of a problem can either be defined as an objective function to be optimize or a constraint that need to be strictly fulfill ()
    - constraint satisfaction problems can be turned into optimiztion problem: instead of requiring perfection, we make an objective function that counts the number of satisfied constraints and considers it to be a thing to maximize
4. The famous NP problems
- categorize problems base on the properties of its solving algorithm. a problem is considered 'easy' if there's a fast solver for it and is considered 'hard' otherwise
#### Properties to consider the hardness of a problem
- problem size: its dimensionality (number of variables, number of values each variable can have)
- running time: the worst-case running time is defined by a formular that is a function of problem size (polynomial if the problem has a short running time or superpolynomial (or exponential) if the problem has longer running time)
- problem reductability: the ability to be transformed into a different problem

#### Class P
- if there exist an algorithm that can solve it in polynomial time. the worst-case running time of the problem of size n is less than $F(n)$ with $F$ be a polynomial formula
- problems of type P is considered 'easy'. e.g: Minimum Spanning Tree problem

#### Class NP
- can be solved (without any running-time guaranteed) by some algorithms and the solution can be (easily) vertified by another algorithm in polynomial time
- (hard to solve, easy to check) e.g: subset-sum problem
    - NP-complete
        - belong to class NP and any other problems in class NP can be reduced to that problem by an algorithm running in polynomial time
    - NP-hard
        - at least as hard as any problems in NP-complete class, and the solution can not necessarily be verified in polynomial time

#### P vs. NP
- the fact that there exists a problem whose solution can't be verified in polynomial time prove that class P is not the same as class NP-hard. what is unknown is that whether the two class P and NP are the same
- (continue...)
- there are huge numbers of practical problems that turns out to be variants of more abstract problems in the NP class. while some easy instances of those problems can be solved in polynomial time, some more complex instances cannot. if we want to grapse the acceptable solutions for all instances, we have to turn to using approximation and metaheuristic to approach such solutions and abandon the idea of providing an exact provably solution that is best for all instances

## 3. Step-by-Step procedure
- Start from a series of (random) individuals with different alleles (or data)
- Calculate the fitness of each individual through an objective function
- Made a selection of the fittest individuals
	- Roulette method: the probability of an individual being chosen to be a parent for the next generation is proportionate to their fitness. This means that the fitter they are, the higher their chance to breed. 
	- Tournament-based selection: fetch random k individuals and let them "compete" with each other, the one with the highest fitness point will be chosen
	- Ranking: order our individuals in a list based on  their fitness. The N individuals with the highest fitness point will be chosen
	- Elitism: generate an offspring that is exactly akin to the individual with the best fitness
	- Steady state selection: eliminate those individuals with lowest fitness point and replace them by the children of those with better fitness.
- Using Genetic Operator to create the new generation
	- Crossover
		- One-point crossover: split the parents' chromosomes into two, the child will take each segment from either of their parents
		- Multipoint crossover: same as One-point crossover, but we will choose multiple split points instead of one
		- Uniform crossover: each allele of the child will be chose randomly from that of their parents. In this method, each allele is treated separately instead of being taken as a whole (segment)
		- Crossover for ordered lists: method of crossover used for some problems with constraint solution to avoid generating invalid solutions. Some of them include:
			- Partially Mapped Crossover (PMC)
			- Cycle Crossover (CX)
			- Order Crossover Operator (OX1)
			- Order-based Crossover Operator (OX2)
	- Mutation
		- Bit-string mutation: flip a bit from a bitstring
		- Random mutation: mutate an allele to a random value
		- Shrink: 
- Return to step 2, iteratively

## 4. Some Notes while using Genetic Algorithm
- Some notes in choosing the parameter in GA
	- There is a trade-off in having a large number of population, you have a large pool in terms of variation but the computer takes more time to calculate the fitness point in each generation so although we need fewer generations to reach our goal, it ends up taking more time
	- If the mutation rate is high, the algorithm will in someway return to the Brute Force Search where everything appears randomly 
- evolutionary searches are often considered as a trade-off between exploration and exploitation
	- exploration is the generation of new individuals in un-tested regions of search space
	- exploitation is the concerntration of searching in the regions of known good solutions
	- 'premature convergence' is the consequence of losing the diversity too quickly --> being trapped in the local optimum 
	- 'anytime behaviour': 

## 5. Related things
- Particle Swarm Optimization