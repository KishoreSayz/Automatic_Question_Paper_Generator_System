import sqlite3

# Connect to the SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('qp.db')
cursor = conn.cursor()

# Create the table for storing questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    question TEXT NOT NULL
)
''')

# Create the table for tracking used questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS used_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    run_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Define the questions for each subject
questions = [
    ('DWDM', 'What is DWDM?'),
    ('DWDM', 'What is data mining?'),
    ('DWDM', 'What is data cleaning?'),
    ('DWDM', 'What is data formatting?'),
    ('DWDM', 'What is a data warehouse?'),
    ('DWDM', 'Write short notes on the following: (a) DATA PREPROCESSING (b) CONCEPT HIERARCHY'),
    ('DWDM', 'Write an algorithm ID3 with sample dataset?'),
    ('DWDM', 'Construct a decision tree for the house owner dataset and apply splitting approach'),
    ('DWDM', 'Explain about schemas of data warehouse?'),
    ('DWDM', 'Q1'),
    ('DWDM', 'Q2'),
    ('DWDM', 'Q3'),
    ('DWDM', 'Q4'),
    ('DWDM', 'Q5'),
    ('DWDM', 'Q6'),
    ('DWDM', 'Q7'),
    ('DWDM', 'Q8'),
    ('CN', 'What is CN?'),
    ('CN', 'Write about LAN, WAN, MAN?'),
    ('CN', 'Write about TCP/IP?'),
    ('CN', 'Write about network topologies?'),
    ('CN', 'Write about unguided media?'),
    ('CN', 'Write about guided media?'),
    ('CN', 'Data link layer and its services and issues?'),
    ('CN', 'Point-to-point protocols'),
    ('CN', 'Explain reference models?'),
    ('CN', 'Briefly explain about framing'),
    ('CN', 'Q1'),
    ('CN', 'Q2'),
    ('CN', 'Q3'),
    ('CN', 'Q4'),
    ('DLD', 'a) i) Convert (8B7.A4)16 to its binary equivalent ii) Convert (714.36)8 to its hexadecimal equivalent'),
    ('DLD', 'Reduce the following Boolean Expression: AB+ABC+AB(D+E)'),
    ('DLD', 'Simplify the following function using K-Map F(A,B,C,D)=∑(0,2,3,8,10,11,12,14)'),
    ('DLD', 'Design a full adder circuit'),
    ('DLD', 'Implement the following Boolean function using 4:1 Mux: F(A,B,C,D)=∑(1,2,5,8,9,12,14)'),
    ('DLD', 'Convert given Gray code (1100110) to its Binary code equivalent.'),
    ('DLD', 'Design full adder using two half adders and one OR gate?'),
    ('DLD', 'Simplify the following function using K-Map: F(A,B,C,D)= ПM(0,1,2,3,5,7,11)'),
    ('DLD', 'What is a multiplexer? Construct a 8:1 multiplexer.'),
    ('DLD', 'Simplify the following 5 Variable function using K-Map: F=∑(0,2,3,5,7,8,10,11,14,15,16,18,24,26,27,29,30,31)?'),
    ('DAA', 'What are the different mathematical notations used for algorithm analysis?'),
    ('DAA', 'Write an algorithm for bubble sort and analyze the algorithm for its time complexity?'),
    ('DAA', 'How to measure the performance of an algorithm? Give some algorithm?'),
    ('DAA', 'Mention the important advantages and disadvantages of using randomized algorithm?'),
    ('DAA', 'What is multi-stage graph with example?'),
    ('DAA', 'Write an algorithm for binary search and analyze the algorithm for its time complexity'),
    ('DAA', 'Mention the differences between dynamic programming and greedy algorithm?'),
    ('DAA', 'Write and explain the control abstraction for divide and conquer approach?'),
    ('DAA', 'Q1'),
    ('DAA', 'Q2'),
    ('DAA', 'Q3'),
    ('DAA', 'Q4'),
    ('IAML', 'Illustrate the various application areas of AI'),
    ('IAML', 'What is learning? Explain learning in neural networks.'),
    ('IAML', 'What is an AI technique? Give its evolution over years.'),
    ('IAML', 'Define neural network. Give its representation.'),
    ('IAML', 'Explain in detail about Knowledge based agents'),
    ('IAML', 'Explain the predicate logic representation and inference in predicate logic with a suitable example.'),
    ('IAML', 'Discuss about pattern representation Propositional Logic.'),
    ('IAML', 'Compare inference in propositional logic with inference in first order logic.'),
    ('IAML', 'Describe the features of Bayesian learning methods.'),
    ('IAML', 'Write about various applications of ML in industry and real world'),
    ('IAML', 'Discuss in detail about K-Nearest neighbour learning.'),
    ('IAML', 'Define Machine Learning. Explain the need and its evolution'),
    ('IAML', 'Q1'),
    ('IAML', 'Q2'),
    ('IAML', 'Q3'),
    ('IAML', 'Q4'),
    ('IAML', 'Q5'),
    ('IAML', 'Q6'),
    ('IAML', 'Q7'),
    ('IAML', 'Q8'),
]

# Insert the questions into the table
cursor.executemany('INSERT INTO questions (subject, question) VALUES (?, ?)', questions)
conn.commit()

# Close the connection
conn.close()
