"use client"
import { useCart } from "@/components/CartContext";
import Link from "next/link";

interface Product {
  _id: string;
  name: string;
  description: string;
  price: number;
  imageUrl: string;
  category: string;
}

interface ProductCardProps {
  product: Product;
}

export default function ProductCard({ product }: ProductCardProps) {
  const { addToCart } = useCart();

  const handleAddToCart = (e: React.MouseEvent) => {
    e.preventDefault(); 
    e.stopPropagation();
    addToCart(product);
  }

  return (
    <Link href={`/product/${product._id}`} className="border rounded-lg p-4 shadow-md hover:shadow-lg transition-shadow flex flex-col">
      <img src={product.imageUrl} alt={product.name} className="w-full h-48 object-cover rounded-md mb-4" />
      <h3 className="text-lg font-semibold flex-grow">{product.name}</h3>
      <div className="flex justify-between items-center mt-4">
        <p className="text-gray-600 text-lg font-bold">${product.price}</p>
        <button onClick={handleAddToCart} className="px-4 py-2 bg-yellow-400 text-black text-sm font-semibold rounded-lg hover:bg-yellow-500 transition-colors">Add to Cart</button>
      </div>
    </Link>
  );
}