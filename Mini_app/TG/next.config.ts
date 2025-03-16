import type { NextConfig } from "next";  

const nextConfig: NextConfig = {  
  async rewrites(){  
    return[  
      {  
        source:'/api/:path*', // Add the leading slash here  
        destination: 'https://127.0.0.1:5328/:path*',  
      },  
    ];  
  },  
  /* config options here */  
  reactStrictMode: true,  

  // Optional: Handle CORS if needed  
  webpack: (config) => {  
    config.resolve.fallback = {   
      fs: false,  // Disable server-side filesystem  
      net: false,  
      tls: false   
    }  
    return config  
  }  
};  

export default nextConfig; 