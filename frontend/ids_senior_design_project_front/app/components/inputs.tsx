import { SelectInputProps, NumberInputProps, CheckInputProps } from '../lib/definitions';

export function NumberInput({label, min, max, step, defaultValue}: NumberInputProps){
    return (
        <div className='flex flex-col gap-2 my-4 '>
            <label htmlFor={label}>{label}</label>
            <input 
                type="number" 
                id={label} 
                name={label} 
                min={min} 
                max={max} 
                step={step} 
                defaultValue={defaultValue}
                className='bg-[#F1F2F6] h-10 w-60 rounded-md px-4 focus:outline-none focus:ring-2 focus:ring-[#1976D2] focus:border-transparent'
            />
        </div>
    );
}

export function CheckInput({label}: CheckInputProps){
    return (
        <div className='flex items-center my-6'>
            <input type="checkbox" id={label} name={label} className='h-4 w-4'/>
            <label htmlFor="scales" className='mx-2 translate-y-[-1.5px]'>{label}</label>
        </div>
    );
}

export function SelectInput({label, values}: SelectInputProps){
    return (
        <div className="w-1/5 flex flex-col gap-2 my-4">
            <label htmlFor="dataset">{label}</label>
            <select className="bg-[#F1F2F6] px-4 rounded-md h-10 focus:outline-none focus:ring-2 focus:ring-[#1976D2] focus:border-transparent">
                {values.map((value: string) => (
                    <option key={value} value={value} className='mt-2 rounded-none'>{value}</option>
                ))}
            </select>
        </div>
    );
}