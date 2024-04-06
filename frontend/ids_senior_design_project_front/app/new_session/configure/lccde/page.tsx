import Form from '@/app/components/config_form';
import Button from '@mui/material/Button';
import { lccdeInputFields } from '@/app/lib/data'

export default function page(){
    return (
        <div>
            <p className="text-xl mb-4"><strong>Configure LCCDE</strong></p>
            <Form dataInputFields={lccdeInputFields}/>
            <Button variant="outlined" href='/new_session'>Go Back</Button>
        </div>
    );
}