# DNAPACManHMM

For this project, we’ll be modifying my DNA Pac-Man game (https://github.com/HussainAther/dnapacman)  to represent how language models (using Hidden Markov Models)
+ Communicate how language models work using the Pac-Man analogy. The next token/letter you eat is the next letter in the sequence of generating a sequence of protein amino acids. 
+ Essentially, if we organize regions of the Pac-Man board representing different hidden states in a Markov Model, then the next letter that Pac-Man eats can represent the next state an HMM selects. We can change the probabilities a certain letter may appear and, when Pac-Man enters the hidden state, then the probabilities would change. 
+ The issue in language models is that the probabilities of which token you eat next depends on what has already happened. 
+ We can use ghosts to represent how you can dissuade the player from choosing certain outcomes over others.
+ See how the probability for different states changes as people play based on which letter they choose next. 

Compare the HMM of Pac-Man to the HMMs in modeling eukaryotic genes: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2766791/

## What are HMMs?

Hidden Markov Models (HMMs) are an extremely versatile statistical representation that can be used to model any set of one-dimensional discrete symbol data. HMMs can model protein sequences in many ways, depending on what features of the protein are represented by the Markov states. They have been extensively used in biological sequence analysis. HMMs have applications in a variety of problems in molecular biology. 

For protein structure prediction, states have been chosen to represent either homologous sequence positions, local or secondary structure types, or transmembrane locality. The resulting models can be used to predict common ancestry, secondary or local structure, or membrane topology by applying one of the two standard algorithms for comparing a sequence to a model. 

For this project, we can focus on three types of HMMs: 
* profile-HMMs
* pair-HMMs
* context-sensitive HMMs

We can compare how HMMs that are used in predicting protein structure relate to the way someone plays a game of Pac-Man. 

## Post-project

After modifying Pac-Man and writing the project, I plan on pitching the article to WIRED titled “How Pac-Man can Predict Proteins.” 
