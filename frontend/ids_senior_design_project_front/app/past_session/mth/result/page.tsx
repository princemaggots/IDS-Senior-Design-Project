'use client'

import { useSearchParams } from 'next/navigation';
import ResultTables from '@/app/components/result_tables';
import Button from '@mui/material/Button';
import ConfirmButton from '@/app/components/confirm_button';
import { useRouter } from 'next/navigation';
import { formatReturnedMthData } from '@/app/lib/format';

export default function Page(){
    const searchParams = useSearchParams();
    const router = useRouter();
    const input = searchParams.get('input');
    const output = searchParams.get('output');
    const pastOutput = searchParams.get('pastOutputData');

    const handleSave = async () => {
        const parsedOutput = JSON.parse(output)
        const parsedInput = JSON.parse(input)
        const returnData = {
            output: parsedOutput,
            input: parsedInput
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/db/save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(returnData)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const responseData = await response.json();
            router.push('/');
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };
    const formattedCurrentData = formatReturnedMthData(output);
    const validJSON = pastOutput.replace(/'/g, '"');
    const formattedPastData = formatReturnedMthData(validJSON);

    return (
        <div>
            <p className="text-xl">Execution Result</p>
            <ResultTables data={formattedCurrentData} pastData={formattedPastData}/>
            <div className='mt-8 flex'>
                <ConfirmButton text={'Discard'} href='/' prompt='Do you want to discard the result?'/>
                <Button variant="contained" style={{marginLeft: 'auto'}} onClick={handleSave} className='bg-primary'>Save</Button>
            </div>
        </div>
    );
}