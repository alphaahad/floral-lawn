import streamlit as st
from PIL import Image
import os, random, io

st.set_page_config(page_title="Floral Lawn Generator", page_icon="🌼", layout="centered")
st.title("🌿 Floral Lawn Wallpaper Generator")
st.markdown("Design your own floral wallpaper 🌸 Choose colors, flowers, and layout style!")


flower_folder = os.path.join(os.path.dirname(__file__), "flowers")

file_map = {
    "Baby’s Breath": "babys_breath.png",
    "Bird of Paradise": "bird_of_paradise.png",
    "Chrysanthemum": "chrysanthemum.png",
    "Gerbera": "gerbera.png",
    "Marigold": "marigold.png",
    "Pink Rose": "pink_rose.png",
    "Tulip Mix": "tulip_mix.png",
    "Forget Me Nots": "forget_me_nots.png",
    "Daffodil": "daffodil.png",
    "Gladiolus": "gladiolus.png",
    "Orchids": "orchids.png",
    "Red Carnation": "red_carnations.png",
    "White Lily": "white_lilies.png",
    "Bluebells": "bluebells.png",
    "Dahlia": "dahlia.png",
    "Iris": "iris.png",
    "Peony": "peonies.png",
    "Rose": "rose.png",
    "White Tulip": "white_tulips.png",
    "Cherry Blossom": "cherry_blossoms.png",
    "Geranium": "geranium.png",
    "Lavender": "lavender.png",
    "Pink Carnation": "pink_carnation.png",
    "Sunflower": "sunflower.png",
    "Yellow Rose": "yellow_rose.png"
}


col1, col2 = st.columns(2)

with col1:
    device_type = st.radio("📱 Wallpaper Type", ["Mobile (1080x1920)", "Laptop/Desktop (1920x1080)"])
    bg_color = st.color_picker("🎨 Pick Background Color", "#fef6f0")

with col2:
    selected_flowers = st.multiselect("🌸 Pick Flower Types (3–10 recommended)", list(file_map.keys()), max_selections=15)

if "Mobile" in device_type:
    canvas_width, canvas_height = 1080, 1920
else:
    canvas_width, canvas_height = 1920, 1080

if st.button("🌼 Generate Wallpaper") and selected_flowers:
    bg = Image.new("RGBA", (canvas_width, canvas_height), bg_color)

    flower_imgs = []
    for flower in selected_flowers:
        path = os.path.join(flower_folder, file_map[flower])
        try:
            img = Image.open(path).convert("RGBA")
            flower_imgs.append(img)
        except Exception as e:
            st.error(f"❌ Could not load {flower}: {e}")

    if not flower_imgs:
        st.warning("No images could be loaded. Please check file names.")
    else:
        tile_size = 140  # ~70% of original
        for y in range(0, canvas_height, tile_size):
            for x in range(0, canvas_width, tile_size):
                flower = random.choice(flower_imgs)
                resized = flower.resize((tile_size, tile_size), Image.LANCZOS)
                bg.paste(resized, (x, y), resized)

        st.image(bg, caption="Your Floral Lawn 🌸", use_container_width=True)
        buf = io.BytesIO()
        bg.save(buf, format="PNG")
        st.download_button("📥 Download Wallpaper", data=buf.getvalue(), file_name="floral_wallpaper.png", mime="image/png")
