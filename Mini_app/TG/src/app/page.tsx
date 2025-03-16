'use client'
import { useState } from "react";
import PhoneLogin from "./Dashboards/phoneLogin";
import Codeconfirm from "./Codeconfirm/codeConfirm"

export default function Home() {
  const [phoneNumber, setPhoneNumber] = useState<string>("");
  return (
    <div className="my-[48px] w-full mx-auto h-[100%] md:w-[720px]">
       <PhoneLogin onChange= {setPhoneNumber}/>
       <Codeconfirm phoneNumber={phoneNumber}/>
    </div>
  );
}
