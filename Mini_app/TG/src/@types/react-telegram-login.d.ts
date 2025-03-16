declare module 'react-telegram-login' {  
    import * as React from 'react';  
  
    interface TelegramLoginButtonProps {  
      dataOnauth: (response: any) => void; // You may further specify the response type as needed  
      botName: string;  
      buttonSize?: number;  
      cornerRadius?: number;  
      theme?: 'light' | 'dark';  
    }  
  
    const TelegramLoginButton: React.FC<TelegramLoginButtonProps>;  
  
    export default TelegramLoginButton;  
  }  