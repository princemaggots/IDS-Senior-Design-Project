import Form from '@/app/components/config_form';
import Button from '@mui/material/Button';
import { treeBasedInputFields } from '@/app/lib/data'

export default function page(){
    return (
        <div>
            <p className="text-xl mb-4"><strong>Configure Tree Based IDS</strong></p>
            <Form dataInputFields={treeBasedInputFields} />
            <Button variant="outlined" href='/new_session' className="translate-y-[-32px]">Go Back</Button>
        </div>
    );
}