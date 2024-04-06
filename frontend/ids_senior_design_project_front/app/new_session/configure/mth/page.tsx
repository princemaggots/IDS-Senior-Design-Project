import Form from "@/app/components/config_form";
import Button from '@mui/material/Button';
import { mthInputFields } from '@/app/lib/data' 

export default function page(){
    return (
        <div>
            <p className="text-xl mb-4"><strong>Configure MTH</strong></p>
            <Form dataInputFields={mthInputFields} />
            <Button  variant="outlined" href='/new_session' className="translate-y-[-32px]">Go Back</Button>
        </div>
    );
}