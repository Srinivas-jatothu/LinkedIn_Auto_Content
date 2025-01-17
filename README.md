# LinkedIn Post Generator

This application assists LinkedIn influencers by generating new posts that align with their past content. Using Few-Shot Learning, it generates new content based on writing style, topics, and other parameters like language and post length.

---

## Key Features

- **Phase 1**: Gather LinkedIn posts and extract important details such as Topic, Language, and Length.
- **Phase 2**: Utilize selected parameters like Topic, Language, and Length to generate fresh posts. The tool applies a few-shot learning approach, analyzing past posts to teach the model the influencer's style of writing.

This tool is especially useful for LinkedIn influencers, like Mohan, who wish to maintain consistency in their posts by creating new content inspired by their previous writing.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [How to Use](#how-to-use)
3. [Features Overview](#features-overview)
4. [Sample Use Case](#sample-use-case)
5. [Contributing](#contributing)
6. [License](#license)

---

## Getting Started

Follow the steps below to set up the tool:

1. **Obtain an API Key**:
   - To use the tool, you'll first need an API key. You can obtain it from [this link](https://console.groq.com/keys).
   
2. **Set up a `.env` file**:
   - Once you have your API key, create a `.env` file in the root directory of the project and include the following line:
     ```bash
     GROQ_API_KEY=your_api_key_here
     ```

3. **Install the Required Dependencies**:
   - Install the necessary libraries by running the following command:
     ```bash
     pip install -r req.txt
     ```

4. **Launch the Streamlit Application**:
   - After installing dependencies, start the Streamlit app using the command:
     ```bash
     streamlit run main.py
     ```

---

## How to Use

### Phase 1: Collecting Data

- **Gather LinkedIn Posts**: The tool collects previous LinkedIn posts from the influencer and extracts key details like Topic, Language, and Length.

### Phase 2: Generating Posts

- **Create New Posts**: After selecting parameters like Topic, Language, and Length, the tool generates a new post. The few-shot learning process uses past posts to guide the model in creating content that reflects the influencer's style.

### Sample Use Case

Consider Mohan, a LinkedIn influencer. He wants to generate a future post that matches his previous writing style. Here's how he can do it:

1. **Upload Past Posts**: Mohan feeds his previous LinkedIn posts into the tool.
2. **Select Parameters**: He chooses a Topic (e.g., "Career Development"), Language (e.g., "English" or "Hinglish"), and post Length (e.g., "Short").
3. **Generate Post**: By pressing the "Generate" button, the tool creates a new post that mirrors his unique writing style.

---

## Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/Srinivas-jatothu/LinkedIn_Auto_Content/main/screenshots/pic1.png" alt="Tool Screenshot 1" style="width: 80%; height: 400px; object-fit: cover; border-radius: 10px;">
</p>
<p align="center" style="font-style: italic; margin-top: 10px; max-width: 80%; text-align: center; font-size: 14px;">
  This is the basic UI created using Streamlit. It consists of a header, input fields for selecting the topic, post length, and language, and a button to generate posts. The UI is clean and user-friendly, allowing users to easily select different parameters for post generation.
</p>

<br>

<p align="center">
  <img src="https://raw.githubusercontent.com/Srinivas-jatothu/LinkedIn_Auto_Content/main/screenshots/Pic2.png" alt="Tool Screenshot 2" style="width: 80%; height: 500px; object-fit: cover; border-radius: 10px;">
</p>
<p align="center" style="font-style: italic; margin-top: 10px; max-width: 80%; text-align: center; font-size: 14px;">
  This is how the output is displayed after the "Generate" button is clicked. The generated post is shown inside a stylish box with a border, which helps highlight the content and makes it easy to read and use directly for LinkedIn posts.
</p>




---


