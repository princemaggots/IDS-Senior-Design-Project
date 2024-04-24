'use client'

import ToggleButton from '@mui/material/ToggleButton';
import ResultPane from './result_pane';
import { useState } from 'react';

export default function ResultTables({data, pastData}: {data: any, pastData?: any}) {
    const [selected, setSelected] = useState(false);
    return (
        <div className='flex flex-col'>
            {pastData && (
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
            )}
            {
                data.map((currentData: any, index: number) => {
                    const correspondingPastData = pastData && pastData[index];
                    return <ResultPane key={index} data={currentData} pastData={correspondingPastData} selected={selected}/>;
                }
            )}
        </div>
    )
}
