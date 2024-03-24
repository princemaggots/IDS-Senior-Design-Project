import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';

const algorithms = [
    { 
        header: 'LCCDE', 
        subHeader: 'Leader Class and Confidence Decision Ensemble', 
        description: 'an ensemble IDS, utilizing XGBoost, LightGBM, and CatBoost to select the best model for each attack class based on performance. It then uses these models and their confidence values for detection decisions.',
        href: './new_session/configure/lccde'
    },
    { 
        header: 'MTH', 
        subHeader: 'Multi-Tiered Hybrid', 
        description: 'an ensemble IDS, utilizing XGBoost, LightGBM, and CatBoost to select the best model for each attack class based on performance. It then uses these models and their confidence values for detection decisions.',
        href: './new_session/configure/mth'
    },
    { 
        header: 'Tree-based', 
        subHeader: 'Tree-based Intelligent IDS', 
        description: 'an ensemble IDS that leverages decision tree, random forest, extra trees, and XGBoost to detect intrusions in both intra-vehicle and external communication networks.',
        href: './new_session/configure/tree_based'
    }
];

export default function page(){
    return (
        <div>
            <p className="text-xl">Select algorithm to test</p>
            {algorithms.map((algorithm, index) => {
                return (
                    <Card key={index} className='mt-8'>
                        <CardContent className='flex mx-6 my-4'>    
                            <div className='w-1/2'>
                                <p className='text-2xl font-bold'>{algorithm.header}</p>
                                <p className='mb-8'>{algorithm.subHeader}</p>
                                <p>{algorithm.description}</p>
                            </div>
                            <div className='ml-auto self-end'>
                                <Button variant="contained" href={algorithm.href}>Configure</Button>
                            </div>
                        </CardContent>
                    </Card>
                );
            })}
        </div>
    );
}