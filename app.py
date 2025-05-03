import streamlit as st
import os
import subprocess
from PIL import Image
from collections import Counter

# Set page title and layout (MUST be the first Streamlit command)
st.set_page_config(page_title="Trending Social Media Styles", layout="wide")

# Custom CSS for Instagram-like styling
st.markdown("""
    <style>
    .main {
        background-color: #F5E9DD;
        padding: 20px;
        text-align: center;
    }
    .stButton>button {
        background-color: #333333;
        color: white;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 16px;
        margin: 10px;
        width: 80%;
        max-width: 300px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .stButton>button:hover {
        background-color: #555555;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }
    .trend-title {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        margin-top: 20px;
    }
    .trend-item {
        font-size: 16px;
        color: #333333;
        margin: 5px 0;
        cursor: pointer;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Paths
TRENDS_FILE = "trends.txt"
PICS_FOLDER = "trending_pics"
SCRAPE_INSTAGRAM_SCRIPT = "scrape_instagram.py"
SCRAPE_X_SCRIPT = "scrape_x.py"
SCRAPE_THREADS_SCRIPT = "scrape_threads.py"

# Check if required files and folders exist
for script in [SCRAPE_INSTAGRAM_SCRIPT, SCRAPE_X_SCRIPT, SCRAPE_THREADS_SCRIPT]:
    if not os.path.exists(script):
        st.error(f"Oops! {script} is missing. Make sure it's in trend_analyzer!")
        st.stop()
if not os.path.exists(PICS_FOLDER):
    os.makedirs(PICS_FOLDER)
    st.info(f"Created {PICS_FOLDER} folder. It's ready to store pictures!")

# Sidebar for scraping and clustering
with st.sidebar:
    st.header("Control Panel")
    # Section 1: Scrape Social Media
    st.subheader("Step 1: Scrape Social Media")
    
    if st.button("Scrape Instagram"):
        with st.spinner("Scraping pictures from Instagram..."):
            try:
                result = subprocess.run(["python", SCRAPE_INSTAGRAM_SCRIPT], capture_output=True, text=True, timeout=300)
                st.success("Instagram scraping complete!")
                st.write("Output:", result.stdout)
                if result.stderr:
                    st.warning(f"Warnings/Errors: {result.stderr}")
            except subprocess.TimeoutExpired:
                st.error("Scraping took too long! Check scrape_instagram.py or try again.")
            except Exception as e:
                st.error(f"Error scraping Instagram: {str(e)}")

    if st.button("Scrape X"):
        with st.spinner("Scraping pictures from X..."):
            try:
                result = subprocess.run(["python", SCRAPE_X_SCRIPT], capture_output=True, text=True, timeout=300)
                st.success("X scraping complete!")
                st.write("Output:", result.stdout)
                if result.stderr:
                    st.warning(f"Warnings/Errors: {result.stderr}")
            except subprocess.TimeoutExpired:
                st.error("Scraping took too long! Check scrape_x.py or try again.")
            except Exception as e:
                st.error(f"Error scraping X: {str(e)}")

    if st.button("Scrape Threads"):
        with st.spinner("Scraping pictures from Threads..."):
            try:
                result = subprocess.run(["python", SCRAPE_THREADS_SCRIPT], capture_output=True, text=True, timeout=300)
                st.success("Threads scraping complete!")
                st.write("Output:", result.stdout)
                if result.stderr:
                    st.warning(f"Warnings/Errors: {result.stderr}")
            except subprocess.TimeoutExpired:
                st.error("Scraping took too long! Check scrape_threads.py or try again.")
            except Exception as e:
                st.error(f"Error scraping Threads: {str(e)}")

    if st.button("Scrape All"):
        with st.spinner("Scraping pictures from Instagram, X, and Threads..."):
            for script, platform in [
                (SCRAPE_INSTAGRAM_SCRIPT, "Instagram"),
                (SCRAPE_X_SCRIPT, "X"),
                (SCRAPE_THREADS_SCRIPT, "Threads")
            ]:
                try:
                    result = subprocess.run(["python", script], capture_output=True, text=True, timeout=300)
                    st.success(f"{platform} scraping complete!")
                    st.write(f"{platform} Output:", result.stdout)
                    if result.stderr:
                        st.warning(f"{platform} Warnings/Errors: {result.stderr}")
                except subprocess.TimeoutExpired:
                    st.error(f"Scraping {platform} took too long! Check the script or try again.")
                except Exception as e:
                    st.error(f"Error scraping {platform}: {str(e)}")

    # Show how many pictures are in trending_pics
    pics = [f for f in os.listdir(PICS_FOLDER) if f.endswith(('.jpg', '.jpeg', '.png'))]
    st.write(f"Found {len(pics)} pictures in {PICS_FOLDER}")

    # Section 2: Label Pictures
    st.subheader("Step 2: Label Pictures")
    if st.button("Label Pictures"):
        if not pics:
            st.error("No pictures found in trending_pics! Scrape some pictures first.")
        else:
            with st.spinner("Labeling pictures..."):
                try:
                    result = subprocess.run(["python", "cluster_pics.py"], capture_output=True, text=True, timeout=300)
                    st.success("Labeling complete!")
                    st.write("Output:", result.stdout)
                    if result.stderr:
                        st.warning(f"Warnings/Errors: {result.stderr}")
                except subprocess.TimeoutExpired:
                    st.error("Labeling took too long! Check cluster_pics.py or try again.")
                except Exception as e:
                    st.error(f"Error labeling pictures: {str(e)}")

# Main content
st.markdown('<div class="header">Trending Social Media Styles</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Discover the Hottest Trends on Social Media</div>', unsafe_allow_html=True)

# Section 3: Display Trends
st.markdown('<div class="trend-title">View Trends</div>', unsafe_allow_html=True)
if not os.path.exists(TRENDS_FILE):
    st.warning(f"{TRENDS_FILE} not found. Label some pictures first!")
else:
    # Read trends from trends.txt (flat list)
    def read_trends():
        trends = []
        with open(TRENDS_FILE, "r") as f:
            lines = f.readlines()
            st.write(f"Total lines in trends.txt: {len(lines)}")  # Debug
            for line in lines:
                line = line.rstrip('\n')
                if not line.strip():
                    st.write("Skipping empty line")  # Debug
                    continue
                st.write(f"Reading line: '{line}'")  # Debug
                if line.startswith("- "):
                    try:
                        if "(labeled as " not in line:
                            st.warning(f"Skipping malformed line (missing label): '{line}'")
                            continue
                        parts = line.split("(labeled as ")
                        if len(parts) != 2:
                            st.warning(f"Skipping malformed line: '{line}'")
                            continue
                        filename = parts[0].replace("- ", "").strip()
                        label = parts[1].strip()
                        if label.endswith(")"):
                            label = label[:-1]
                        pic_path = os.path.join(PICS_FOLDER, filename)
                        st.write(f"Found picture: {filename}, label: {label}, path: {pic_path}")  # Debug
                        if not os.path.exists(pic_path):
                            st.warning(f"Picture not found: {pic_path}")
                            continue
                        trends.append({
                            "filename": filename,
                            "label": label,
                            "path": pic_path
                        })
                    except Exception as e:
                        st.warning(f"Error parsing line '{line}': {str(e)}")
                else:
                    st.warning(f"Unexpected line format: '{line}'")
        return trends

    trends = read_trends()
    if not trends:
        st.warning("No trends found in trends.txt. Check the file or label again!")
    else:
        # Find the "highest trends" (most common labels)
        labels = [trend["label"].split(",")[0] for trend in trends]
        label_counts = Counter(labels)
        most_common_label, most_common_count = label_counts.most_common(1)[0]
        st.subheader(f"Highest Trend: {most_common_label} ({most_common_count} images)")

        # Show images for the highest trend directly
        highest_trend_images = [trend for trend in trends if trend["label"].split(",")[0] == most_common_label]
        if highest_trend_images:
            cols = st.columns(4)
            for i, trend in enumerate(highest_trend_images):
                try:
                    img = Image.open(trend["path"])
                    with cols[i % 4]:
                        st.image(img, caption=f"{trend['label']} ({trend['filename']})", width=150)
                except Exception as e:
                    st.warning(f"Could not load {trend['filename']}: {str(e)}")
        else:
            st.warning(f"No images found for {most_common_label}. Check trends.txt!")

        # Show all trends with images directly
        st.subheader("All Trends")
        st.write(f"Found {len(trends)} trending images")
        cols = st.columns(4)
        for i, trend in enumerate(trends):
            try:
                img = Image.open(trend["path"])
                with cols[i % 4]:
                    st.image(img, caption=f"{trend['label']} ({trend['filename']})", width=150)
            except Exception as e:
                st.warning(f"Could not load {trend['filename']}: {str(e)}")

# Debug: Show contents of trends.txt
if st.checkbox("Show contents of trends.txt"):
    if os.path.exists(TRENDS_FILE):
        with open(TRENDS_FILE, "r") as f:
            st.text("trends.txt contents:")
            st.text(f.read())
    else:
        st.warning("trends.txt not found!")