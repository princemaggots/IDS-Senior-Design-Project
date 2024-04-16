import CircularIndeterminate from '@/app/components/circular_indeterminate';
import { Suspense } from 'react';
import ResultTables from '@/app/components/result_tables';
import Button from '@mui/material/Button';
import ConfirmButton from '@/app/components/confirm_button';

export default function page(){
    return (
        <div>
            <p className="text-xl">Execution Result</p>
            <Suspense fallback={<CircularIndeterminate />}>
                <ResultTables />
                <div className='mt-8 flex'>
                    <ConfirmButton text={'Discard'} href='/' prompt='Do you want to discard the result?'/>
                    <Button variant="contained" style={{marginLeft: 'auto'}} className='bg-primary'>Save</Button>
                </div>
            </Suspense>
        </div>
    );
}