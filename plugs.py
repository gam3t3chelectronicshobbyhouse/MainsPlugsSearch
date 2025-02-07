import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Requires Pillow

# Dictionary mapping countries to the primary plug types used there.
plug_data = {
    "Afghanistan": ["Type C", "Type D"],
    "Albania": ["Type C", "Type F"],
    "Algeria": ["Type C", "Type F"],
    "Andorra": ["Type C", "Type F"],
    "Angola": ["Type C", "Type F"],
    "Argentina": ["Type C", "Type I"],
    "Armenia": ["Type C"],
    "Australia": ["Type I"],
    "Austria": ["Type C", "Type F"],
    "Azerbaijan": ["Type C", "Type F"],
    "Bahamas": ["Type A", "Type B"],
    "Bahrain": ["Type G"],
    "Bangladesh": ["Type C", "Type D", "Type G", "Type K"],
    "Barbados": ["Type A", "Type B"],
    "Belarus": ["Type C", "Type F"],
    "Belgium": ["Type C", "Type E"],
    "Belize": ["Type A", "Type B"],
    "Benin": ["Type C", "Type E", "Type F"],
    "Bhutan": ["Type C", "Type D"],
    "Bolivia": ["Type A", "Type C", "Type L"],
    "Bosnia and Herzegovina": ["Type C", "Type F"],
    "Botswana": ["Type D", "Type M"],
    "Brazil": ["Type N", "Type C"],
    "Brunei": ["Type G"],
    "Bulgaria": ["Type C", "Type F"],
    "Burkina Faso": ["Type C", "Type E", "Type F"],
    "Burundi": ["Type C", "Type E", "Type F"],
    "Cambodia": ["Type A", "Type C", "Type G"],
    "Cameroon": ["Type C", "Type E", "Type F"],
    "Canada": ["Type A", "Type B"],
    "Chile": ["Type C", "Type L"],
    "China": ["Type A", "Type I"],
    "Colombia": ["Type A", "Type B", "Type C"],
    "Costa Rica": ["Type A", "Type B"],
    "Croatia": ["Type C", "Type F"],
    "Cuba": ["Type A", "Type B"],
    "Cyprus": ["Type G"],
    "Czech Republic": ["Type C", "Type E", "Type F"],
    "Denmark": ["Type C", "Type K"],
    "Dominican Republic": ["Type A", "Type B"],
    "Ecuador": ["Type A", "Type B"],
    "Egypt": ["Type C", "Type F"],
    "El Salvador": ["Type A", "Type B"],
    "Estonia": ["Type C", "Type F"],
    "Ethiopia": ["Type C", "Type E", "Type F"],
    "Finland": ["Type C", "Type F"],
    "France": ["Type C", "Type E"],
    "Gabon": ["Type C", "Type E", "Type F"],
    "Gambia": ["Type C", "Type D"],
    "Georgia": ["Type C"],
    "Germany": ["Type C", "Type F"],
    "Ghana": ["Type D", "Type G"],
    "Greece": ["Type C", "Type F"],
    "Guatemala": ["Type A", "Type B"],
    "Haiti": ["Type A", "Type B"],
    "Honduras": ["Type A", "Type B"],
    "Hong Kong": ["Type G"],
    "Hungary": ["Type C", "Type F"],
    "Iceland": ["Type C", "Type F"],
    "India": ["Type C", "Type D", "Type M"],
    "Indonesia": ["Type C", "Type F", "Type G"],
    "Iran": ["Type C", "Type D", "Type F"],
    "Iraq": ["Type C", "Type D", "Type G"],
    "Ireland": ["Type G"],
    "Israel": ["Type C", "Type H"],
    "Italy": ["Type C", "Type F", "Type L"],
    "Jamaica": ["Type A", "Type B"],
    "Japan": ["Type A", "Type B"],
    "Jordan": ["Type C", "Type D", "Type F", "Type G"],
    "Kazakhstan": ["Type C", "Type F"],
    "Kenya": ["Type G"],
    "Kuwait": ["Type G"],
    "Kyrgyzstan": ["Type C", "Type F"],
    "Laos": ["Type A", "Type B", "Type I"],
    "Latvia": ["Type C", "Type F"],
    "Lebanon": ["Type C", "Type D", "Type G"],
    "Lesotho": ["Type M"],
    "Liberia": ["Type A", "Type B"],
    "Libya": ["Type C", "Type D"],
    "Lithuania": ["Type C", "Type F"],
    "Luxembourg": ["Type C", "Type F"],
    "Macedonia": ["Type C", "Type F"],
    "Madagascar": ["Type C", "Type E", "Type F"],
    "Malawi": ["Type G"],
    "Malaysia": ["Type G"],
    "Maldives": ["Type G"],
    "Mali": ["Type C", "Type E", "Type F"],
    "Malta": ["Type G"],
    "Mauritania": ["Type C", "Type E", "Type F"],
    "Mauritius": ["Type C", "Type G"],
    "Mexico": ["Type A", "Type B"],
    "Moldova": ["Type C", "Type F"],
    "Monaco": ["Type C", "Type E"],
    "Mongolia": ["Type C", "Type D"],
    "Montenegro": ["Type C", "Type F"],
    "Morocco": ["Type C", "Type E", "Type F"],
    "Mozambique": ["Type C", "Type F"],
    "Myanmar": ["Type A", "Type C", "Type D", "Type F", "Type G"],
    "Namibia": ["Type D", "Type M"],
    "Nepal": ["Type C", "Type D"],
    "Netherlands": ["Type C", "Type F"],
    "New Zealand": ["Type I"],
    "Nicaragua": ["Type A", "Type B"],
    "Nigeria": ["Type D", "Type G"],
    "North Korea": ["Type C"],
    "Norway": ["Type C", "Type F"],
    "Oman": ["Type G"],
    "Pakistan": ["Type C", "Type D", "Type G"],
    "Panama": ["Type A", "Type B"],
    "Papua New Guinea": ["Type I"],
    "Paraguay": ["Type A", "Type B", "Type C", "Type L"],
    "Peru": ["Type A", "Type B", "Type C"],
    "Philippines": ["Type A", "Type B", "Type C"],
    "Poland": ["Type C", "Type E", "Type F"],
    "Portugal": ["Type C", "Type F"],
    "Qatar": ["Type G"],
    "Romania": ["Type C", "Type F"],
    "Russia": ["Type C", "Type F"],
    "Rwanda": ["Type C", "Type E", "Type F"],
    "Saudi Arabia": ["Type A", "Type B", "Type G"],
    "Senegal": ["Type C", "Type E", "Type F"],
    "Serbia": ["Type C", "Type F"],
    "Singapore": ["Type G"],
    "Slovakia": ["Type C", "Type E", "Type F"],
    "Slovenia": ["Type C", "Type F"],
    "South Africa": ["Type M", "Type N"],
    "South Korea": ["Type C", "Type F"],
    "Spain": ["Type C", "Type F"],
    "Sri Lanka": ["Type D", "Type G"],
    "Sudan": ["Type C", "Type D"],
    "Sweden": ["Type C", "Type F"],
    "Switzerland": ["Type C", "Type J", "Type L", "Type M"],
    "Syria": ["Type C", "Type D", "Type G"],
    "Taiwan": ["Type A", "Type B"],
    "Tajikistan": ["Type C", "Type F"],
    "Tanzania": ["Type D", "Type G"],
    "Thailand": ["Type A", "Type B", "Type C", "Type O"],
    "Togo": ["Type C", "Type E", "Type F"],
    "Trinidad and Tobago": ["Type A", "Type B"],
    "Tunisia": ["Type C", "Type E", "Type F"],
    "Turkey": ["Type C", "Type F"],
    "Turkmenistan": ["Type C", "Type F"],
    "Uganda": ["Type G"],
    "Ukraine": ["Type C", "Type F"],
    "United Arab Emirates": ["Type G"],
    "United Kingdom": ["Type G"],
    "United States": ["Type A", "Type B"],
    "Uruguay": ["Type C", "Type F"],
    "Uzbekistan": ["Type C", "Type F"],
    "Vanuatu": ["Type I"],
    "Vatican City": ["Type C", "Type F"],
    "Venezuela": ["Type A", "Type B"],
    "Vietnam": ["Type A", "Type C", "Type D", "Type G"],
    "Yemen": ["Type A", "Type B", "Type G"],
    "Zambia": ["Type C", "Type D", "Type G"],
    "Zimbabwe": ["Type D", "Type G"],
}

# Compatibility mapping: which plug types are considered alternates (compatible)
# For example, Type E and Type F are generally cross-compatible.
compatibility = {
    "Type E": ["Type F"],
    "Type F": ["Type E"],
    # Additional compatibility rules can be added here.
}

# Dictionary mapping each plug type to its grounding status.
plug_grounding = {
    "Type A": "NG",  # Two flat pins; typically ungrounded.
    "Type B": "GND", # Three flat pins with a grounding pin.
    "Type C": "NG",  # Two round pins; no ground.
    "Type D": "NG",  # Three round pins; generally ungrounded.
    "Type E": "GND", # Two round pins with a hole for the earth pin.
    "Type F": "GND", # Schuko plug – two round pins with grounding clips.
    "Type G": "GND", # Three rectangular pins with ground.
    "Type H": "GND", # Used in Israel – includes grounding.
    "Type I": "GND", # Used in Australia/New Zealand – includes ground.
    "Type J": "GND", # Swiss plug – typically grounded.
    "Type K": "GND", # Danish plug – typically grounded.
    "Type L": "GND", # Italian plug – typically grounded.
    "Type M": "NG",  # Similar to Type D; generally ungrounded.
    "Type N": "GND", # Brazilian plug – includes ground.
    "Type O": "GND", # Thai plug – includes ground.
}

# Dictionary mapping plug types to image file paths.
plug_images = {
    "Type A": "images/type_a.png",
    "Type B": "images/type_b.png",
    "Type C": "images/type_c.png",
    "Type D": "images/type_d.png",
    "Type E": "images/type_e.png",
    "Type F": "images/type_f.png",
    "Type G": "images/type_g.png",
    "Type H": "images/type_h.png",
    "Type I": "images/type_i.png",
    "Type J": "images/type_j.png",
    "Type K": "images/type_k.png",
    "Type L": "images/type_l.png",
    "Type M": "images/type_m.png",
    "Type N": "images/type_n.png",
    "Type O": "images/type_o.png",
}


def show_plug_image(plug_type):
    """Open a new window to display the image for the given plug type, with auto-close and a close button."""
    image_file = plug_images.get(plug_type)

    if not image_file:
        messagebox.showerror("Image Error", f"No image available for {plug_type}.")
        return

    try:
        img = Image.open(image_file)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize for consistency
        img_tk = ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Image Error", f"Error loading image for {plug_type}: {e}")
        return

    # Create a new window to show the image
    top = tk.Toplevel(root)
    top.title(f"{plug_type} Image")

    # Keep a reference to prevent garbage collection
    top.img_tk = img_tk

    # Display the image
    label = tk.Label(top, image=top.img_tk)
    label.pack(padx=10, pady=10)

    # Close button
    close_btn = tk.Button(top, text="Close", command=top.destroy)
    close_btn.pack(pady=5)

    # Auto-close after 30 seconds
    top.after(30000, top.destroy)
def on_plug_double_click(event):
    """When a plug type is double-clicked, extract its type and show its image."""
    widget = event.widget
    selection = widget.curselection()
    if selection:
        index = selection[0]
        item_text = widget.get(index)  # e.g., "Type A (NG)"
        # Extract the plug type (everything before the " (")
        plug_type = item_text.split(" (")[0]
        show_plug_image(plug_type)

def search_plug():
    """Search for plug types for the entered country and update the listboxes."""
    country_input = country_entry.get().strip()
    if not country_input:
        messagebox.showwarning("Input Error", "Please enter a country name.")
        return

    # Perform a case-insensitive search for the country.
    found_key = None
    for key in plug_data:
        if key.lower() == country_input.lower():
            found_key = key
            break

    if found_key:
        primary_plugs = plug_data[found_key]
        # Determine alternate plug types based on compatibility rules.
        alternate_plugs = set()
        for plug in primary_plugs:
            if plug in compatibility:
                for alt in compatibility[plug]:
                    if alt not in primary_plugs:
                        alternate_plugs.add(alt)

        # Clear the listboxes.
        primary_listbox.delete(0, tk.END)
        alternate_listbox.delete(0, tk.END)

        # Insert primary plug types with grounding info.
        for plug in primary_plugs:
            status = plug_grounding.get(plug, "Unknown")
            primary_listbox.insert(tk.END, f"{plug} ({status})")

        # Insert alternate plug types with grounding info.
        for plug in sorted(alternate_plugs):
            status = plug_grounding.get(plug, "Unknown")
            alternate_listbox.insert(tk.END, f"{plug} ({status})")
    else:
        messagebox.showerror("Not Found", "No plug information found for that country.")
        primary_listbox.delete(0, tk.END)
        alternate_listbox.delete(0, tk.END)

# -----------------------------
# Set up the main application window.
# -----------------------------
root = tk.Tk()
root.title("Mains Plugs Search")
root.geometry("300x400")
root.resizable(False, False)

# Country input.
tk.Label(root, text="Enter Country:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
country_entry = tk.Entry(root, width=15)
country_entry.grid(row=0, column=1, padx=10, pady=5)

# Search button.
search_button = tk.Button(root, text="Search", command=search_plug)
search_button.grid(row=1, column=0, columnspan=2, pady=10)

# Listbox for primary plug types.
tk.Label(root, text="Primary Plug Types:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
primary_listbox = tk.Listbox(root, width=40, height=6)
primary_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
primary_listbox.bind("<Double-Button-1>", on_plug_double_click)

# Listbox for alternate plug types.
tk.Label(root, text="Alternate Plug Types:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
alternate_listbox = tk.Listbox(root, width=40, height=4)
alternate_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
alternate_listbox.bind("<Double-Button-1>", on_plug_double_click)

root.mainloop()
