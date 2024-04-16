import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { models } from '../lib/data';

export default function page(){
    return (
        <div>
            <p className="text-xl"><strong>Select algorithm to test</strong></p>
            {models.map((model, index) => {
                return (
                    <Card key={index} className='mt-8'>
                        <CardContent className='flex mx-6 my-4'>    
                            <div className='w-1/2'>
                                <p className='text-2xl font-bold'>{model.header}</p>
                                <p className='mb-8'>{model.subHeader}</p>
                                <p>{model.description}</p>
                            </div>
                            <div className='ml-auto self-end'>
                                <Button variant="contained" href={model.href}>Configure</Button>
                            </div>
                        </CardContent>
                    </Card>
                );
            })}
            <Button variant="outlined" href='/' className='mt-6'>Go Back</Button>
        </div>
    );
}