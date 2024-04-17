'use client'

import { useSearchParams } from 'next/navigation'
import ResultTables from '@/app/components/result_tables';
import Button from '@mui/material/Button';
import ConfirmButton from '@/app/components/confirm_button';
import { useRouter } from 'next/navigation';

export default function Page(){
    const searchParams = useSearchParams()
    const data = searchParams.get('data')
    const router = useRouter();
    
    const handleSave = async () => {
        const parsedData = JSON.parse(data)
        const returnData = {
            output: parsedData
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/db/save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(returnData)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const responseData = await response.json();
            console.log(responseData);
            router.push('/');
            // Handle the response data as needed
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };

    let formattedData;
    if (data !== null) {
        const parsedData = JSON.parse(data);
        formattedData = [
            {
                model: 'XGBoost',
                acc_score: parsedData.xb_acc_score,
                class_f1: [
                    {attackClass: '0 BENIGN', value: parsedData.xb_class_f1[0]},
                    {attackClass: '1 Bot', value: parsedData.xb_class_f1[1]},
                    {attackClass: '2 Brute Force', value: parsedData.xb_class_f1[2]},
                    {attackClass: '3 DoS', value: parsedData.xb_class_f1[3]},
                    {attackClass: '4 Infiltration', value: parsedData.xb_class_f1[4]},
                    {attackClass: '5 PortScan', value: parsedData.xb_class_f1[5]},
                    {attackClass: '6 WebAttack', value: parsedData.xb_class_f1[6]},
                ],
                class_report: parsedData.xb_class_report,
                confusion_matrix: parsedData.xb_confusion_matrix,
                f1: parsedData.xb_f1,
                prec_score: parsedData.xb_prec_score,
                rec_score: parsedData.xb_rec_score
            },
            {
                model: 'LightGBM',
                acc_score: parsedData.lg_acc_score,
                class_f1: [
                    {attackClass: '0 BENIGN', value: parsedData.lg_class_f1[0]},
                    {attackClass: '1 Bot', value: parsedData.lg_class_f1[1]},
                    {attackClass: '2 Brute Force', value: parsedData.lg_class_f1[2]},
                    {attackClass: '3 DoS', value: parsedData.lg_class_f1[3]},
                    {attackClass: '4 Infiltration', value: parsedData.lg_class_f1[4]},
                    {attackClass: '5 PortScan', value: parsedData.lg_class_f1[5]},
                    {attackClass: '6 WebAttack', value: parsedData.lg_class_f1[6]},
                ],
                class_report: parsedData.lg_class_report,
                confusion_matrix: parsedData.lg_confusion_matrix,
                f1: parsedData.lg_f1,
                prec_score: parsedData.lg_prec_score,
                rec_score: parsedData.lg_rec_score
            },
            {
                model: 'CatBoost',
                acc_score: parsedData.cb_acc_score,
                class_f1: [
                    {attackClass: '0 BENIGN', value: parsedData.cb_class_f1[0]},
                    {attackClass: '1 Bot', value: parsedData.cb_class_f1[1]},
                    {attackClass: '2 Brute Force', value: parsedData.cb_class_f1[2]},
                    {attackClass: '3 DoS', value: parsedData.cb_class_f1[3]},
                    {attackClass: '4 Infiltration', value: parsedData.cb_class_f1[4]},
                    {attackClass: '5 PortScan', value: parsedData.cb_class_f1[5]},
                    {attackClass: '6 WebAttack', value: parsedData.cb_class_f1[6]},
                ],
                class_report: parsedData.cb_class_report,
                confusion_matrix: parsedData.cb_confusion_matrix,
                f1: parsedData.cb_f1,
                prec_score: parsedData.cb_prec_score,
                rec_score: parsedData.cb_rec_score
            },
            {
                model: 'Stack',
                acc_score: parsedData.stack_acc_score,
                class_f1: [
                    {attackClass: '0 BENIGN', value: parsedData.stack_class_f1[0]},
                    {attackClass: '1 Bot', value: parsedData.stack_class_f1[1]},
                    {attackClass: '2 Brute Force', value: parsedData.stack_class_f1[2]},
                    {attackClass: '3 DoS', value: parsedData.stack_class_f1[3]},
                    {attackClass: '4 Infiltration', value: parsedData.stack_class_f1[4]},
                    {attackClass: '5 PortScan', value: parsedData.stack_class_f1[5]},
                    {attackClass: '6 WebAttack', value: parsedData.stack_class_f1[6]},
                ],
                f1: parsedData.stack_f1,
                prec_score: parsedData.stack_prec_score,
                rec_score: parsedData.stack_rec_score
            }
        ];
    }

    return (
        <div>
            <p className="text-xl">Execution Result</p>
            <ResultTables data={formattedData}/>
            <div className='mt-8 flex'>
                <ConfirmButton text={'Discard'} href='/' prompt='Do you want to discard the result?'/>
                <Button variant="contained" style={{marginLeft: 'auto'}} onClick={handleSave} className='bg-primary'>Save</Button>
            </div>
        </div>
    );
}