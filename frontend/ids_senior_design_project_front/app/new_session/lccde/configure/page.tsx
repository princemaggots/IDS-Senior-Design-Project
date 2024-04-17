'use client'

import Form from '@/app/components/config_form';
import Button from '@mui/material/Button';
import { lccdeInputFields } from '@/app/lib/data';
import { useState } from 'react';
import CircularIndeterminate from '@/app/components/circular_indeterminate';
import { useRouter } from 'next/navigation';

export default function Page(){
    const [isLoading, setIsLoading] = useState(false);
    const [loadingMessage, setLoadingMessage] = useState('Training model, please wait...');
    const router = useRouter();

    const handleSubmit = async (formData: any) => {
        setIsLoading(true);
        setLoadingMessage('Initializing model...');
    
        try {
            setLoadingMessage('Training model, please wait...');
            const response = await fetch('http://127.0.0.1:8000/engine/lccde_run', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
        
            if (!response.ok) {
                throw new Error(`HTTP error ${response.status}`);
            }
        
            const data = await response.json();
            console.log(data);
            router.push(`/new_session/lccde/result?data=${encodeURIComponent(JSON.stringify(data))}`);
        } catch (error) {
            console.error('Error submitting form:', error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div>
            <p className="text-xl mb-4">
                <strong>Configure LCCDE</strong>
            </p>
            <Form dataInputFields={lccdeInputFields} onSubmit={handleSubmit} />
            <Button variant="outlined" href="/new_session">
                Go Back
            </Button>
            {isLoading && (
                <div className="fixed top-0 left-0 w-full h-full bg-white flex flex-col justify-center items-center">
                    <CircularIndeterminate />
                    <p className="mt-4 text-lg text-gray-900">{loadingMessage}</p>
                </div>
            )}
        </div>
    );
}