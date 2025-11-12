'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { ShoppingCart, Home, Info, Menu, X, ShoppingBag } from 'lucide-react'

export function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)

  // ✅ Detect scroll for dynamic background
  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20)
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const navLinks = [
    { href: '/', label: 'Home', icon: <Home size={18} /> },
    { href: '/about', label: 'About', icon: <Info size={18} /> },
    { href: '/shop', label: 'Shop', icon: <ShoppingBag size={18} /> },
    { href: '/cart', label: 'Cart', icon: <ShoppingCart size={18} /> },
  ]

  return (
    <nav
      className={`fixed top-0 left-0 w-full z-50 transition-all duration-300 h-18 ${
        isScrolled ? 'bg-black/50 backdrop-blur-md shadow-md' : 'bg-black/30'
      }`}
    >
      <div className="max-w-7xl mx-auto flex justify-between items-center px-5 text-white">
        <Link href="/">
          <Image
            src="/images/logo.png" 
            alt="WatchesStore Logo"
            width={200} height={200}
            priority 
            className="relative top-2 md:top-3 w-28 h-auto"/>
        </Link>

        {/* ✅ Desktop Menu */}
        <div className="hidden md:flex gap-8">
          {navLinks.map((link) => (
            <Link key={link.href} href={link.href}
              className="flex items-center gap-1 hover:text-gray-300 transition">
              {link.icon} {link.label}
            </Link>
          ))}
        </div>

        {/* ✅ Mobile Menu Button */}
        <div className="md:hidden">
          <button onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
            className="focus:outline-none hover:text-gray-300 transition">
            {isMenuOpen ? <X size={26} /> : <Menu size={26} />}
          </button>
        </div>
      </div>

      {/* ✅ Mobile Dropdown Menu */}
      <div
        className={`md:hidden flex flex-col items-center bg-black/30 backdrop-blur-md top-0 text-white gap-5 py-6 transition-all duration-300 overflow-hidden ${
          isMenuOpen ? 'max-h-80 opacity-100' : 'max-h-0 opacity-0'
        }`}
      >
        {navLinks.map((link) => (
          <Link
            key={link.href}
            href={link.href}
            className="flex items-center gap-2 text-lg hover:text-gray-300 transition"
            onClick={() => setIsMenuOpen(false)}
          >
            {link.icon}
            {link.label}
          </Link>
        ))}
      </div>
    </nav>
  )
}
