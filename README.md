# V.I.S.I.O.N. (Vision-based Insight System for Influencer and Online Networks)
V.I.S.I.O.N. (Vision-based Insight System for Influencer and Online Networks) is an AI-powered system designed to detect and forecast visual trends across social media platforms. Leveraging Vision Transformers and Reinforcement Learning (RL) agents, V.I.S.I.O.N. analyzes influencer content, generates trend insights using Retrieval-Augmented Generation (RAG), and provides marketers with real-time data and adaptive strategy suggestions to stay ahead in the fast-paced world of social media marketing.
Features

Trend Detection: Uses Vision Transformers to analyze images from social media platforms like Instagram, X, and Threads to identify emerging visual trends.
Trend Forecasting: Employs RL agents to predict future trends based on historical and real-time data.
Influencer Content Analysis: Scrapes and processes influencer content to uncover patterns and styles driving engagement.
Insight Generation: Utilizes RAG to generate actionable insights for marketers.
Real-Time Data: Pulls live data from social media platforms for up-to-date trend analysis.
Adaptive Strategy Suggestions: Offers tailored marketing strategies based on detected trends and forecasts.
User-Friendly Interface: A Streamlit-based web app for easy interaction and visualization of trends.

Project Structure

app.py: Main Streamlit application for the user interface, displaying trends and scraped images.
analyze_pics.py: Script for analyzing scraped images using Vision Transformers.
cluster_pics.py: Script for clustering images and labeling them with detected trends.
scrape_instagram.py: Script to scrape images from Instagram.
scrape_x.py: Script to scrape images from X.
scrape_threads.py: Script to scrape images from Threads.
trends.html: HTML template for rendering trends (if applicable).
trends.txt: File storing labeled trends after clustering.
imagenet_labels.txt: Predefined labels for image classification.
trending_pics/: Directory to store scraped images.
static/: Directory for static assets (e.g., CSS, JS) used in the web app.
templates/: Directory for HTML templates (if applicable).
chromedriver-win32/: WebDriver for scraping (Windows 32-bit version).

Installation

Clone the Repository:
git clone https://github.com/your-username/vision-trend-analyzer.git
cd vision-trend-analyzer


Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Ensure you have Python 3.8+ installed. Then, install the required packages:
pip install -r requirements.txt

Note: If requirements.txt is not provided, install the following core dependencies:
pip install streamlit pillow numpy torch torchvision transformers scikit-learn selenium


Install ChromeDriver:

The project uses Selenium for scraping. Ensure ChromeDriver is installed and matches your Chrome browser version.
The repository includes chromedriver-win32 for Windows 32-bit systems. For other systems, download the appropriate version from ChromeDriver Downloads and place it in the project root or update the path in the scraping scripts.


Set Up Environment Variables (if applicable):

Some scraping scripts may require API keys or credentials for social media platforms. Set these as environment variables or in a .env file.



Usage

Run the Streamlit App:
streamlit run app.py

This will launch the web app in your default browser.

Scrape Social Media:

Use the sidebar in the Streamlit app to scrape images from Instagram, X, or Threads individually or all at once.
Images are saved in the trending_pics directory.


Label Pictures:

After scraping, click "Label Pictures" to cluster and label the images using Vision Transformers.
Results are stored in trends.txt.


View Trends:

The app automatically displays the highest trend and all detected trends with their respective images in a grid layout.



Example Output
After scraping and labeling, the app might show trends like:

Highest Trend: "Jean" (3 images)
All Trends: Displays all scraped images with labels such as "Jean," "Jersey," "Projector," etc., in a 4-column grid.

Technologies Used

Python: Core programming language.
Streamlit: For the web app interface.
Vision Transformers (ViT): For image analysis and trend detection (via torch and transformers).
Reinforcement Learning: For trend forecasting (implemented in analyze_pics.py).
RAG (Retrieval-Augmented Generation): For generating marketing insights.
Selenium: For web scraping with ChromeDriver.
PIL (Pillow): For image processing.
Scikit-learn: For clustering images.
Counter (collections): For identifying the most common trends.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to your branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, please open an issue on GitHub or contact your-email@example.com.

Stay ahead of the curve with V.I.S.I.O.N. – Where Trends Meet Tomorrow!
