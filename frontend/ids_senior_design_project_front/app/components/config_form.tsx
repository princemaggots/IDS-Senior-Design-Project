'use client'

import { SelectInput, NumberInput } from "./inputs";
import { datasetFields } from '../lib/data';
import { usePathname } from 'next/navigation';

import { useState } from "react";
import { NumberInputProps, SelectInputProps } from "@/app/lib/definitions"

export default function Form({dataInputFields}: {dataInputFields: any}){
    const pathname = usePathname()
    const paths = pathname.split('/')
    const model = paths[paths.length - 1]

    const initialFormState = dataInputFields.reduce((acc: Record<string, number>, field: NumberInputProps) => {
        acc[field.name] = field.defaultValue;
        return acc;
    }, {});

    const [formState, setFormState] = useState({
        dataset: 'CICIDS2017',
        model: model,
        ...initialFormState,
    });

    const handleSelectChange = (name:string, value: string) => {
        setFormState({
            ...formState,
            [name]: value,
        });
    };
    
    const handleNumberChange = (name:string, value: number) => {
        setFormState({
            ...formState,
            [name]: value,
        });
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log(formState)

        // api_path = 
        // try {
        //     // replace the mock api path to the actual api path
        //     const response = await fetch('https://66157f68b8b8e32ffc7b1be3.mockapi.io/api/configs', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json'
        //         },
        //         body: JSON.stringify(formState)
        //     });
        
        //     if (!response.ok) {
        //         throw new Error(`HTTP error. status: ${response.status}`);
        //     }

        //     const responseData = await response.json();
        //     router.push('/new_session/result');
        // } catch (error) {
        //     console.error('Error submitting form:', error);
        // }
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col">
            <SelectInput 
                {...datasetFields}
                onChange={handleSelectChange}
            />
            <div className="flex flex-wrap gap-x-10 my-10">
                {dataInputFields.map((input: NumberInputProps | SelectInputProps, index: number) => (
                    input.type == 'number' ?
                        (<NumberInput 
                            key={index} 
                            {...input as NumberInputProps}
                            onChange={handleNumberChange}
                        />) : (
                        <SelectInput
                            key={index}
                            {...input as SelectInputProps}
                            onChange={handleSelectChange}
                        />)
                ))}
            </div>
            <button className="bg-primary rounded-[5px] h-8 w-24 text-white self-end shadow-lg hover:bg-[#0e5499] transition-colors duration-[400ms]">Run</button>
        </form>
    );
}