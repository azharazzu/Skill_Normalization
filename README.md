# Skill_Normalization

# Content
- [Application Description](#Application-Description)
- [Technology Used](#Technology-Used)
- [Business model](#Business-model)
- [Methodology](#Methodology)
- [Input](#Input)
- [Output](#Output)
- [Example](#Example)
- [Postman API](#Postman-API)

# Application description

### The Skill Normalization service is used to convert raw Skills into standard Skills. The developed model removes all unwanted or unnecessary things, such as punctuation, versions, emojis from the raw skills.

# **Technology Used**

### Python, Transformers, Flask, Sklearn

# **Business model**

### Each user have different ways of writing about the same thing, with the help of Skill normalization each Skill can be converted into one of the standard output Skills which can be further used for Skill recommendation or Title2skill relationship.

# Methodology

![Untitled](https://user-images.githubusercontent.com/101692969/234448714-3f78c76f-b324-4533-a2f2-881d484abae8.png)

1. **Collected raw skills from LinkedIn and other sources.**
2. **Preprocessing involves the emojis, Stop-Words, non english titles and duplicates removal and convert into key sensitive.**
3. **After preprocessing apply stemming and lemmatization on skills data to make standardization.**
4. **Manually verified the skills to prepare the training data.**

<img width="483" alt="Untitled (1)" src="https://user-images.githubusercontent.com/101692969/234448757-773f71ba-0ed2-405b-b64d-eb1d39e64cf1.png">

6. **Facebook bart base model is trained on these 64k dataset and the loss value was around 0.02.**
7.  **Streamlit and postman api is developed in which the input is raw title and output is standard    title**

# Input

- **Raw Skills**

# Output

- **Standard  Skills**

# Example
![Untitled (2)](https://user-images.githubusercontent.com/101692969/234448800-c07ba497-b811-42d1-b83f-08981dc91778.png)
![Untitled (3)](https://user-images.githubusercontent.com/101692969/234448828-80fe268b-1317-43b3-b088-7baf903538d1.png)


# Postman Api
Postman URl: http://127.0.0.1:5000/skill_norm
![image](https://user-images.githubusercontent.com/101692969/234567578-64b357e9-bd4b-45e9-b56e-9f09a6732b72.png)
![image](https://user-images.githubusercontent.com/101692969/234567957-44c00310-bbf7-49d0-8f69-fe6f13060791.png)


