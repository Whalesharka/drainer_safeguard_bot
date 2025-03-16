
import React from 'react'
import Image from 'next/image'
import headImage from "@/assets/pro-6.jpg"

interface PropsType {
    phoneNumber : string;
}
const Codeconfirm: React.FC<PropsType>= ({phoneNumber}) =>{
      
    const getCode =() =>{

    }  
    return(
        <div className='flex flex-col items-center text-center'>
            <div>
             <Image
              src={headImage}
              alt='Verify Logo'
              className='w-[120px] h-[120px] md:w-[160px] md:g-[160px] rounded-[50%]' 
             />
             <p className='text-[20px] text-[#FFFFFF] font-bold mt-[20px] md:text-[32px]'> +{phoneNumber}</p>
             </div>
             <div className='mt-[20px]'>  
                <p className='text-[#AAAAAA] text-[14px] md:text-[16px]'>We have sent you a message in Telegram</p>
                <p className='text-[#AAAAAA] text-[14px] md:text-[16px]'>with the code.</p>
             </div>
            <form onSubmit={getCode} className='flex flex-col w-[360px] mt-[30px]'>
                <input placeholder='Code' className='bg-[#212121] h-[54px] rounded-[10px] pl-[10px] hover:border-[#8774e1]'/>
                <button type='submit' className='mt-[20px]'>Please send code</button> 
            </form>
        </div>
    )
}

export default Codeconfirm;