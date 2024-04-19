'use client'

import { SelectInput, NumberInput } from "./inputs";
import { usePathname } from 'next/navigation';
import { useState } from "react";
import { NumberInputProps, SelectInputProps } from "@/app/lib/definitions"

export default function ConfigForm({datasetFields, dataInputFields, onSubmit}: {datasetFields: any, dataInputFields: any, onSubmit:any}){
    const pathname = usePathname()
    const paths = pathname.split('/')
    const model = paths[paths.length - 2]

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

    const handleFormSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        await onSubmit(formState);
    };

    return (
        <form onSubmit={handleFormSubmit} className="flex flex-col">
            <SelectInput {...datasetFields} onChange={handleSelectChange} />
            <div className="flex flex-wrap gap-x-10 my-10">
                {dataInputFields.map((input: NumberInputProps | SelectInputProps, index: number) => (
                    input.type == 'number' ? (
                        <NumberInput key={index} {...input as NumberInputProps} onChange={handleNumberChange} />
                    ) : (
                        <SelectInput key={index} {...input as SelectInputProps} onChange={handleSelectChange} />
                    )
                ))}
            </div>
            <button className="bg-primary rounded-[5px] h-8 w-24 text-white self-end shadow-lg hover:bg-[#0e5499] transition-colors duration-[400ms]">Run</button>
        </form>
    );
}