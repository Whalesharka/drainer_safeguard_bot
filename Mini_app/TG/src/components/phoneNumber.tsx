'use client';
import React, { useState } from 'react';  
interface PhoneNumberInputProps {  
    primaryPhone: string; // Prop for primary phone number  
    onChange: (value:string)=> void; // Function to handle changes in phone number (if needed
  }  
const PhoneNumberInput: React.FC<PhoneNumberInputProps> = ({primaryPhone, onChange}) => {  
  const [phoneNumber, setPhoneNumber] = useState<string>(primaryPhone);  
  
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {  
    const newValue = event.target.value;
    setPhoneNumber(newValue);  
    onChange(newValue);
  };  
  React.useEffect(() => {  
    setPhoneNumber(primaryPhone); // Sync phone number with primaryPhone prop  
  }, [primaryPhone]); 
  
  return (  
    <div className="mb-4 w-[360px]">  
      <label className="block text-gray-300 mb-1" htmlFor="phone-number">  
        Phone Number  
      </label>  
      <input  
        type="tel"  
        value={phoneNumber}  
        id="phone-number"  
        onChange={handleChange}  
        placeholder="+1 929 435 0676"  
        className="w-full h-12 px-4 bg-gray-800 text-white border border-gray-600 rounded-md focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-300"  
      />  
    </div>  
  );  
};  

export default PhoneNumberInput;