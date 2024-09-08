
# Conversational Image Recognition Chatbot

This project is a Conversational Image Recognition Chatbot that uses a combination of image recognition and natural language processing (NLP) to recognize objects in uploaded images and engage in meaningful conversation with users about the recognized objects.

## Project Overview

The chatbot leverages the ResNet50 model for image recognition and the GPT-2 model for natural language processing to answer questions about the uploaded image. Users can upload an image, and the chatbot will identify objects and respond to any questions they ask based on those objects.

## Features

- Upload images and get object recognition results.
- Ask questions about the recognized objects, and the chatbot will generate meaningful responses.
- Uses TensorFlow for image recognition and Hugging Face Transformers for text generation.
- Simple and intuitive web interface built with Streamlit.

## Prerequisites

Before running the project, ensure you have the following tools and libraries installed:

- Python 3.7 or later
- Pip (Python package installer)
- Virtual Environment (optional but recommended)

Required Python libraries:

pip install tensorflow
pip install transformers
pip install opencv-python
pip install streamlit
pip install numpy
pip install Pillow
pip install scikit-learn

## Dataset

This project uses the COCO Dataset (Common Objects in Context) for object recognition. You can download the dataset from the [COCO Dataset website](https://cocodataset.org/#download).

Organize the dataset in a directory structure that can be accessed by the image recognition model.

## Directory Structure


conversational_image_recognition_chatbot/
│
├── image_recognition.py        # Image recognition logic
├── nlp_model.py                # NLP model logic for conversation
├── main.py                     # Main application script
├── README.md                   # Project README file
│
├── env/                        # Virtual environment (optional)
├── coco/                       # COCO dataset (optional)
│   ├── annotations/
│   ├── train2017/
│   └── val2017/
│
└── images/                     # Directory for sample images


## Running the Project

1. Clone the repository:


git clone https://github.com/hindhupriya/conversational_image_recognition_chatbot.git
cd conversational_image_recognition_chatbot


2. Set up a virtual environment (optional but recommended):


python -m venv env
source env/bin/activate  # On Windows: `env\Scripts\activate`

3. Install the required dependencies:


pip install -r requirements.txt


4. Download and organize the COCO Dataset as explained in the prerequisites.

5. Run the chatbot application using Streamlit:

streamlit run main1.py


## Usage

- Upload an image using the web interface.
- The chatbot will identify objects in the image.
- Type a question about the image, and the chatbot will respond.

## Example

Upload an image of a dog, and the chatbot may identify the dog with a certain confidence level (e.g., "Golden Retriever (85.67%)"). You can then ask questions like, "What kind of dog is this?" or "Is this a pet?"

## Customization

- Improve Image Recognition: You can fine-tune the ResNet50 model on specific datasets for better accuracy in your use case.
- Improve NLP Responses: You can fine-tune GPT-2 or use a different language model for more specific or context-aware responses.
- Multi-Language Support: Add support for other languages using translation APIs or multilingual models.

## Deployment

To deploy the chatbot, consider using cloud platforms such as:

- AWS (Amazon Web Services)
- Google Cloud
- Heroku

Follow the platform's deployment instructions for Python or Streamlit applications.

## Future Enhancements

- Fine-tune both the image recognition and NLP models for improved accuracy.
- Implement multi-language support.
- Add more security and scalability features for large-scale use cases.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
