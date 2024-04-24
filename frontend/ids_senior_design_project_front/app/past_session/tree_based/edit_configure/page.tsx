'use client'

import ConfigForm from '@/app/components/config_form';
import Button from '@mui/material/Button';
import { treeBasedInputFields } from '@/app/lib/data';
import { useState } from 'react';
import CircularIndeterminate from '@/app/components/circular_indeterminate';
import { useRouter } from 'next/navigation';
import { useSearchParams } from 'next/navigation';
import { datasetFields } from '@/app/lib/data';

export default function Page() {
    const [isLoading, setIsLoading] = useState(false);
    const [loadingMessage, setLoadingMessage] = useState('Training model, please wait...');
    const router = useRouter();
    const searchParams = useSearchParams()
    const inputData = searchParams.get('input');
    const pastOutputData = searchParams.get('output')

    const validJSON = inputData.replace(/'/g, '"');
    const inputObj = JSON.parse(validJSON);
    treeBasedInputFields.map(field => {
        field.defaultValue = inputObj[field.name];
    });

    datasetFields.defaultValue = inputObj.dataset;

    const handleSubmit = async (formData: any) => {
        setIsLoading(true);
        setLoadingMessage('Initializing model...');
    
        try {
            setLoadingMessage('Training model, please wait...');
            const response = await fetch('http://127.0.0.1:8000/engine/treebased_run', {
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

            router.push(`/past_session/tree_based/result?output=${encodeURIComponent(JSON.stringify(data))}&input=${encodeURIComponent(JSON.stringify(formData))}&pastOutputData=${encodeURIComponent(pastOutputData)}`);        
        } catch (error) {
            console.error('Error submitting form:', error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div>
            <p className="text-xl mb-4">
                <strong>Edit Configuration for Tree Based</strong>
            </p>
            <ConfigForm datasetFields={datasetFields} dataInputFields={treeBasedInputFields} onSubmit={handleSubmit} />
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
    )
}
