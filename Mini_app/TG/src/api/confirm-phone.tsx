import type { NextApiRequest, NextApiResponse } from "next";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method === "POST") {
        const {country, phoneNumber} = req.body;
        res.status(200).json({message: 'Phonenumber received', country, phoneNumber});   
    } else {
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    } 
}
