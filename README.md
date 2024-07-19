
Healthcare Assistant


Overview
Healthcare Assistant is an advanced application designed to streamline and enhance the management of healthcare information. The application integrates multiple features including a search engine powered by GPT-4, drug label detection, prescription reading, a medicine recommendation system, and a reminders system to ensure you never miss your medications.

Features
Search Engine: Leverages GPT-4 API to provide accurate and detailed responses to healthcare-related queries.


Drug Label Detection: Uses optical character recognition (OCR) to detect and read drug labels from images.

Prescription Reader: Extracts and interprets information from prescription documents.

Medicine Recommendation System: Provides personalized medicine recommendations based on user inputs and medical history.

Reminders System: Sends notifications to remind users to take their medications on time.



## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/openapi
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id-(GPT-4)}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Appendix

Any additional information goes here


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Screenshots


https://drive.google.com/file/d/1c2WiGSJQ4cnoHJqOIRBP1yS7IXPmtyW0/view?usp=drive_link
## Deployment

Running the Application

Using Streamlit, Run the Streamlit App
streamlit run main.py

Access the Application
Open your web browser and navigate to http://localhost:8501.


Fork the Repository
git clone https://github.com/nehachitral/healthcare-assistant.git
cd healthcare-assistant
Create a Branch

git checkout -b feature/new-feature
Commit Changes

git add .
git commit -m 'Add some new feature'
Push to Branch

git push origin feature/new-feature
Create a Pull Request


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Feedback

Detailed Features
1. Search Engine
Functionality: Enter healthcare-related queries and get responses powered by GPT-4.
Usage: Type your query into the search bar and click "Search".


2. Drug Label Detection
Functionality: Upload an image of a drug label to read the text using PaddleOCR.
Usage: Click on "Drug Label Detection", upload an image, and view the detected text.

3. Prescription Reader
Functionality: Upload a prescription document to extract and interpret the information.
Usage: Click on "Prescription Reader", upload the document, and view the extracted details.

4. Medicine Recommendation System
Functionality: Enter your symptoms or condition to get personalized medicine recommendations.
Usage: Click on "Medicine Recommendations", provide the necessary information, and receive recommendations.

5. Reminders System
Functionality: Set and manage reminders for your medication schedule.
Usage: Click on "Reminders", set your medication schedule, and receive timely notifications.


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/neha-chitral-0b0a81250)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


## Tech Stack

**Client:** streamlit

**Server:** Python with flask


## Demo

https://drive.google.com/file/d/1c2WiGSJQ4cnoHJqOIRBP1yS7IXPmtyW0/view?usp=drive_link


## Documentation

[Documentation](https://linktodocumentation)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Installation
Prerequisites
Python 3.8 or higher
Virtual environment tool (e.g., venv or conda)


Steps
Clone the Repository:
git clone https://github.com/nehachitral/healthcare-assistant.git

cd healthcare-assistant
Set Up a Virtual Environment


python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install Dependencies:

pip install -r requirements.txt
Install PaddleOCR
pip install paddlepaddle paddleocr

Set Up Environment Variables
Create a .env file in the root directory and add your GPT-4 API key:

GPT4_API_KEY=your_openai_api_key
```
    