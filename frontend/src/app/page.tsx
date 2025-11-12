import Image from "next/image";

export default function Home() {
  return (
    <div className="w-full min-h-screen bg-gradient-to-l from-gray-950 via-blue-900 to-gray-800
      flex flex-col items-center justify-center text-amber-400">

      {/* 3D PERSPECTIVE WRAPPER */}
      <div 
        className="group [perspective:1200px]" 
        data-aos="zoom-in"
        data-aos-duration="1200"
      >
        <div className="relative transition-transform duration-700 ease-out 
          group-hover:[transform:rotateY(18deg)_rotateX(8deg)_scale(1.05)]">
          
          <Image
            src="/images/hero.png"
            alt="Watch hero image"
            width={420}
            height={420}
            className="animate-3dFloat drop-shadow-[0_15px_25px_rgba(0,0,0,0.45)]"
          />
        </div>
      </div>
    </div>
  );
}
