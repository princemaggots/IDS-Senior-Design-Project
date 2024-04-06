import { SelectInput, NumberInput } from "./inputs";
import { datasetFields } from '../lib/data';

export default function Form({dataInputFields}: {dataInputFields: any}){
    return (
        <form className="flex flex-col">
            <SelectInput type={datasetFields.type} description={datasetFields.description} label={datasetFields.label} values={datasetFields.values}/>
            <div className="flex flex-wrap gap-x-10 my-10">
                {dataInputFields.map((input:any, index: number) => (
                    <NumberInput key={index} {...input}/>
                ))}
            </div>
            <button className="bg-primary rounded-[5px] h-8 w-24 text-white self-end shadow-lg hover:bg-[#0e5499] transition-colors duration-[400ms]">Run</button>
        </form>
    );
}