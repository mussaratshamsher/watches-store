from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from typing import List

class Product(BaseModel):
    id: int
    image: str
    name: str
    price: float
    tags: List[str]
    availability: bool
    details: str

class Box(BaseModel):
    id: int
    image: str
    name: str
    price: float
    tags: List[str]
    availability: bool
    details: str

app = FastAPI()

# Mount the 'static' directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Sample product data
products = {
    1: Product(id=1,image="/static/images/img1.jpg", name="Classic Chronograph", price=250.00, tags=["classic", "chronograph", "leather"], availability=True,
        details="A timeless piece with a leather strap and stainless steel case.Water Resistant & its Perfect for any occasion."), 
    2: Product(id=2,image="/static/images/img2.jpg", name="Sporty Digital", price=150.00, tags=["sporty", "digital", "rubber"], availability=True,
        details="A rugged digital watch with a rubber strap and multiple functions, including stopwatch and alarm. Ideal for active lifestyles."),
    3: Product(id=3,image="/static/images/img3.jpg", name="Elegant Dress Watch", price=300.00, tags=["elegant", "dress", "metal"], availability=False,
        details="A sleek and sophisticated dress watch with a metal bracelet and minimalist design. Perfect for formal occasions."),
    4: Product(id=4,image="/static/images/img4.jpg", name="Vintage Mechanical", price=400.00, tags=["vintage", "mechanical", "leather"], availability=True,
        details="A classic mechanical watch with a leather strap and intricate detailing. A nod to traditional watchmaking."),
    5: Product(id=5,image="/static/images/img5.jpg", name="Smartwatch Pro", price=350.00, tags=["smartwatch", "fitness", "touchscreen"], availability=True,
        details="A modern smartwatch with fitness tracking features, touchscreen display, and customizable watch faces. Great for tech enthusiasts."),
    6: Product(id=6,image="/static/images/img6.jpg", name="Diver's Watch", price=500.00, tags=["diver", "waterproof", "stainless steel"], availability=False,
        details="A robust diver's watch with high water resistance, luminous hands, and a stainless steel case. Built for underwater adventures."), 
    7: Product(id=7,image="/static/images/img7.jpg", name="Aviator Watch", price=275.00, tags=["aviator", "chronograph", "leather"], availability=True,
        details="A pilot-inspired watch with a chronograph function, leather strap, and large, easy-to-read dial. Ideal for aviation enthusiasts."),
    8: Product(id=8,image="/static/images/img8.jpg", name="Minimalist Watch", price=200.00, tags=["minimalist", "simple", "metal"], availability=True,
        details="A sleek and simple watch with a metal mesh band and minimalist design. Perfect for everyday wear."),
    9: Product(id=9,image="/static/images/img9.jpg", name="Luxury Gold Watch", price=1000.00, tags=["luxury", "gold", "leather"], availability=True,    
        details="A luxurious gold-plated watch with a leather strap and elegant design. A statement piece for special occasions."),
    10: Product(id=10,image="/static/images/img10.jpg", name="Casual Everyday Watch", price=120.00, tags=["casual", "everyday", "rubber"], availability=True,
        details="A versatile and durable everyday watch with a rubber strap and simple design. Suitable for all occasions."),   
    11: Product(id=11,image="/static/images/img11.jpg", name="Retro Digital Watch", price=180.00, tags=["retro", "digital", "plastic"], availability=True,
        details="A fun and nostalgic digital watch with a plastic case and retro design. Features include alarm and backlight."),
    12: Product(id=12,image="/static/images/img12.jpg", name="Field Watch", price=220.00, tags=["field", "rugged", "leather"], availability=False,
        details="A durable field watch with a leather strap, luminous hands, and a rugged design. Built for outdoor adventures."),
    13: Product(id=13,image="/static/images/img13.jpg", name="Skeleton Watch", price=450.00, tags=["skeleton", "mechanical", "metal"], availability=True,
        details="A unique skeleton watch with a metal bracelet and visible mechanical movement. A blend of artistry and engineering."),
    14: Product(id=14,image="/static/images/img14.jpg", name="Tactical Watch", price=320.00, tags=["tactical", "military", "rubber"], availability=True,
        details="A tough tactical watch with a rubber strap, multiple time zones, and a durable design. Ideal for military and outdoor use."),
    15: Product(id=15,image="/static/images/img15.jpg", name="Fashion Watch", price=130.00, tags=["fashion", "trendy", "plastic"], availability=True,
        details="A trendy fashion watch with a plastic case and colorful design. Perfect for adding a pop of color to any outfit."),    
    16: Product(id=16,image="/static/images/img16.jpg", name="Chronograph Sport Watch", price=280.00, tags=["chronograph", "sport", "leather"], availability=True,
        details="A sporty chronograph watch with a leather strap and multiple dials. Great for timing activities."),
    17: Product(id=17,image="/static/images/img17.jpg", name="Hybrid Smartwatch", price=330.00, tags=["hybrid", "smartwatch", "metal"], availability=True,
        details="A hybrid smartwatch with a metal bracelet, analog display, and smart features like notifications and fitness tracking."),
    18: Product(id=18,image="/static/images/img18.jpg", name="Luxury Dive Watch", price=800.00, tags=["luxury", "dive", "stainless steel"], availability=False,
        details="A high-end luxury dive watch with a stainless steel case, high water resistance, and elegant design. Perfect for both diving and formal wear."),
    19: Product(id=19,image="/static/images/img19.jpg", name="Classic Leather Watch", price=210.00, tags=["classic", "leather", "simple"], availability=True,
        details="A classic leather watch with a simple design and comfortable strap. Suitable for everyday wear."),
    20: Product(id=20,image="/static/images/img20.jpg", name="Outdoor Adventure Watch", price=260.00, tags=["outdoor", "adventure", "rubber"], availability=True,
        details="A rugged outdoor adventure watch with a rubber strap, compass, and durable design. Built for exploring the great outdoors."),
    21: Product(id=21,image="/static/images/img21.jpg", name="Automatic Watch", price=370.00, tags=["automatic", "mechanical", "metal"], availability=True,
        details="A sophisticated automatic watch with a metal bracelet and intricate mechanical movement. A perfect blend of style and craftsmanship."),
    22: Product(id=22,image="/static/images/img22.jpg", name="Digital Sports Watch", price=160.00, tags=["digital", "sports", "plastic"], availability=True,
        details="A durable digital sports watch with a plastic case, stopwatch, and backlight. Ideal for athletes and fitness enthusiasts."),
    23: Product(id=23,image="/static/images/img23.jpg", name="Elegant Silver Watch", price=290.00, tags=["elegant", "silver", "leather"], availability=True,
        details="An elegant silver watch with a leather strap and sophisticated design. Perfect for formal occasions."),
    24: Product(id=24,image="/static/images/img24.jpg", name="Rugged Field Watch", price=240.00, tags=["rugged", "field", "rubber"], availability=False,
        details="A tough rugged field watch with a rubber strap, luminous hands, and durable design. Built for outdoor adventures."),    
}

#Sample box data
boxes ={
    1: Box(id=1,image="/static/images/box1.jpg", name="Classic Chronograph Box", price=270.00, tags=["classic", "chronograph", "leather"], availability=True,
        details="Includes the Classic Chronograph watch, a leather strap, and a stainless steel case. Comes with a stylish box and warranty."), 
    2: Box(id=2,image="/static/images/box2.jpg", name="Sporty Digital Box", price=170.00, tags=["sporty", "digital", "rubber"], availability=True,
        details="Includes the Sporty Digital watch, a rubber strap, and multiple functions like stopwatch and alarm. Comes with a sporty box and warranty."),
    3: Box(id=3,image="/static/images/box3.jpg", name="Elegant Dress Watch Box", price=320.00, tags=["elegant", "dress", "metal"], availability=False,
        details="Includes the Elegant Dress Watch, a metal bracelet, and minimalist design. Comes with an elegant box and warranty."),
    4: Box(id=4,image="/static/images/box4.jpg", name="Vintage Mechanical Box", price=420.00, tags=["vintage", "mechanical", "leather"], availability=True,
        details="Includes the Vintage Mechanical watch, a leather strap, and intricate detailing. Comes with a vintage-style box and warranty."),   
} 

# API Endpoint --1
# for products
@app.get("/products", response_model=List[Product])
async def get_products():
    return list(products.values())
# Get product by ID
@app.get("/products/{id}", response_model=Product)
async def get_product(id: int):
    return boxes[id]

# API Endpoint --2
#for boxes
@app.get("/boxes", response_model=List[Box])
async def get_boxes():
    return list(boxes.values())
# Get box by ID
@app.get("/boxes/{id}", response_model=Box)
async def get_box(id: int):
    return boxes[id]
