import Form from "@/app/components/config_form";
import { mthInputFields } from '@/app/lib/data' 
import ConfirmButton from '@/app/components/confirm_button';

export default function page(){
    return (
        <div>
            <p className="text-xl mb-4"><strong>Configure MTH</strong></p>
            <Form dataInputFields={mthInputFields} />
            <ConfirmButton text={'Go Back'} className="translate-y-[-32px]" href='/new_session' prompt='Do you want to discard the configuration?'/>
        </div>
    );
}