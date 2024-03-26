import { SelectInput, CheckInput, NumberInput } from "./inputs";
import Button from '@mui/material/Button';

export default function Form(){
    return (
        <form>
            <SelectInput label={'Select Dataset'} values={['CICIDS2017', 'Car-Hacking']}/>
            <div className="flex gap-10">
                <CheckInput label={'Display attack labels'}/>
                <CheckInput label={'Display class count'}/>
            </div>
            <div className="flex flex-wrap gap-10">
                <NumberInput label={'Number of clusters'} min={1} max={30} step={1} defaultValue={20}/>
            </div>
            <Button variant="contained">Run</Button>
        </form>
    );
}