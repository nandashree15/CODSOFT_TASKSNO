def get_response(user_input):
    user_input = user_input.lower().strip()

    # ---------------- GREETINGS ----------------
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! 😊 I'm your educational chatbot. You can ask me about AI, Machine Learning, Deep Learning, Python, and Computer Science."

    # ---------------- ABOUT CHATBOT ----------------
    elif "your name" in user_input or "who are you" in user_input:
        return "I am an intelligent rule-based educational chatbot created for the CodSoft AI Internship."

    elif "what can you do" in user_input or "what do you do" in user_input:
        return "I can answer predefined questions about Artificial Intelligence, Machine Learning, Deep Learning, Python, and general Computer Science topics."

    # ---------------- ARTIFICIAL INTELLIGENCE ----------------
    elif (
        "what is ai" in user_input
        or "what is artificial intelligence" in user_input
        or "define ai" in user_input
        or "define artificial intelligence" in user_input
        or "explain ai" in user_input
    ):
        return "Artificial Intelligence (AI) is a field of computer science that enables machines to perform tasks that normally require human intelligence, such as learning, reasoning, problem-solving, and decision-making."

    elif "applications of ai" in user_input or "uses of ai" in user_input:
        return "AI is used in healthcare, education, finance, transportation, robotics, recommendation systems, virtual assistants, cybersecurity, and many other fields."

    elif "types of ai" in user_input:
        return "The commonly discussed types of AI are Narrow AI, General AI, and Super AI. Narrow AI is designed for specific tasks, while General AI refers to human-level intelligence across many tasks."

    # ---------------- MACHINE LEARNING ----------------
    elif (
    "machine learning" in user_input
    or user_input == "ml"
):
        return "Machine Learning (ML) is a branch of AI where computers learn patterns from data and use those patterns to make predictions or decisions without being explicitly programmed for every task."

    elif "types of machine learning" in user_input or "types of ml" in user_input:
        return "The three common types of Machine Learning are supervised learning, unsupervised learning, and reinforcement learning."

    elif "supervised learning" in user_input:
        return "Supervised learning uses labeled training data. The model learns the relationship between inputs and known outputs to make predictions on new data."

    elif "unsupervised learning" in user_input:
        return "Unsupervised learning works with unlabeled data. It finds hidden patterns or groups in the data, such as through clustering."

    elif "reinforcement learning" in user_input:
        return "Reinforcement learning is a type of Machine Learning where an agent learns by interacting with an environment and receiving rewards or penalties."

    # ---------------- DEEP LEARNING ----------------
    elif (
        "what is deep learning" in user_input
        or "define deep learning" in user_input
        or "explain deep learning" in user_input
        or user_input == "dl"
    ):
        return "Deep Learning is a type of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns from large amounts of data."

    elif "neural network" in user_input:
        return "A neural network is a computing model inspired by the human brain. It contains interconnected nodes called neurons that process information and learn patterns from data."

    elif "cnn" in user_input or "convolutional neural network" in user_input:
        return "CNN stands for Convolutional Neural Network. It is commonly used for image processing, computer vision, and image classification."

    elif "rnn" in user_input or "recurrent neural network" in user_input:
        return "RNN stands for Recurrent Neural Network. It is designed to work with sequential data such as text, speech, and time-series data."

    # ---------------- PYTHON ----------------
    elif (
        "what is python" in user_input
        or "define python" in user_input
        or "explain python" in user_input
        or user_input == "python"
    ):
        return "Python is a high-level, general-purpose programming language known for its simple and readable syntax. It is widely used in AI, Machine Learning, Data Science, Web Development, and Automation."

    elif "python features" in user_input or "features of python" in user_input:
        return "Important Python features include simple syntax, readability, portability, a large standard library, object-oriented programming support, and a large ecosystem of libraries."

    elif "python list" in user_input or "what is a list in python" in user_input:
        return "A Python list is an ordered and mutable collection that can store multiple values. Example: numbers = [10, 20, 30]."

    elif "python dictionary" in user_input or "what is dictionary in python" in user_input:
        return "A Python dictionary stores data as key-value pairs. Example: student = {'name': 'Nandashree', 'age': 20}."

    elif "python function" in user_input or "what is a function in python" in user_input:
        return "A function in Python is a reusable block of code designed to perform a particular task. It is defined using the 'def' keyword."

    # ---------------- COMPUTER SCIENCE ----------------
    elif "what is computer science" in user_input or "define computer science" in user_input:
        return "Computer Science is the study of computers, computational systems, algorithms, programming, data, software, and the principles behind computing."

    elif "what is algorithm" in user_input or "define algorithm" in user_input:
        return "An algorithm is a step-by-step procedure used to solve a problem or perform a specific task."

    elif "what is database" in user_input or "define database" in user_input:
        return "A database is an organized collection of data that can be stored, managed, accessed, and updated efficiently."

    elif "what is dbms" in user_input or "define dbms" in user_input:
        return "DBMS stands for Database Management System. It is software used to create, store, organize, retrieve, and manage data in databases."

    elif "what is operating system" in user_input or "define operating system" in user_input:
        return "An Operating System is system software that manages computer hardware and software resources and provides services for applications."

    elif "what is data structure" in user_input or "define data structure" in user_input:
        return "A data structure is a way of organizing and storing data so that it can be accessed and processed efficiently. Examples include arrays, stacks, queues, linked lists, trees, and graphs."

    # ---------------- COMPARISONS ----------------
    elif "difference between ai and ml" in user_input:
        return "AI is the broader concept of machines performing intelligent tasks, while Machine Learning is a subset of AI that allows systems to learn patterns from data."

    elif "difference between machine learning and deep learning" in user_input:
        return "Machine Learning uses various algorithms to learn from data, while Deep Learning uses multi-layer neural networks and is especially useful for complex data such as images, audio, and text."

    elif "difference between python and java" in user_input:
        return "Python emphasizes simple and readable syntax and is widely used in AI and data science. Java is a strongly typed, object-oriented language commonly used for enterprise software, Android development, and large applications."

    # ---------------- GENERAL CONVERSATION ----------------
    elif "how are you" in user_input:
        return "I'm doing great! 😊 Thanks for asking."

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! 😊 Feel free to ask me another question."

    elif "help" in user_input:
        return "You can ask me questions such as: What is AI? What is Machine Learning? What is Deep Learning? What is Python? What is a database? What is an algorithm?"

    # ---------------- GOODBYE ----------------
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! 👋 Keep learning and have a great day!"
    elif "database" in user_input or "databases" in user_input:
        return "A database is an organized collection of data that can be stored, managed, and retrieved efficiently. Examples include MySQL, PostgreSQL, Oracle, and MongoDB." 
    
    # ---------------- UNKNOWN INPUT ----------------
    else:
        return "I'm sorry, I don't have a predefined answer for that yet. Try asking me about AI, Machine Learning, Deep Learning, Python, or Computer Science."


# ---------------- CHAT LOOP ----------------

