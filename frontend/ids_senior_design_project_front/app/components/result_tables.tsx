'use client'

import ToggleButton from '@mui/material/ToggleButton';
import ResultPane from './result_pane';
import { useState, useEffect } from 'react';
import { OutputData } from '@/script/seed';
import { modelToAlgorithms, algorithmFullName } from '@/app/lib/data';
import { usePathname  } from 'next/navigation';

export default function ResultTables() {
    const [selected, setSelected] = useState(false);
    // const [resultData, setResultData] = useState([]);
    const pathname = usePathname();
    const model = pathname.split('/')[2];
    // const algorithms: string[] = modelToAlgorithms[model];

    // fetch results
    // useEffect(() => {
    //     fetch('https://66157f68b8b8e32ffc7b1be3.mockapi.io/api/records')
    //     .then(response => response.json())
    //     .then(data => setResultData(data))
    //     .catch(error => console.error('Error fetching data:', error));
    // }, [selected]);

    // const filterDataByModel = (modelPrefix: string) => {
    //     return Object.keys(OutputData).reduce((acc, key) => {
    //         if (key.startsWith(modelPrefix)) {
    //             acc[key] = OutputData[key];
    //         }
    //         return acc;
    //     }, {});
    // };

    return (
        <div className='flex flex-col'>
            <ToggleButton
                value="check"
                selected={selected}
                onChange={() => {
                    setSelected(!selected);
                }}
                className='self-end bg-primary text-white hover:bg-[#0e5499] transition-colors duration-[400ms]'
                color='primary'
                >
                Compare
            </ToggleButton>
            {/* {algorithms.map((algorithm: string, index) => (
                <ResultPane key={index} algorithm={algorithm} data={filterDataByModel(algorithm)} />
            ))} */}
        </div>
    )
}
