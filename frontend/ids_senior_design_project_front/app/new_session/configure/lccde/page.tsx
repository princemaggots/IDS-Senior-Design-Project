import Form from '@/app/components/config_form';
import Button from '@mui/material/Button';

export default function page(){
    return (
        <div>
            <p className="text-xl">Configure LCCDE</p>
            <Form />
            <Button variant="outlined" href='/new_session'>Go Back</Button>
        </div>
    );
}