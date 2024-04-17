'use client'

import ToggleButton from '@mui/material/ToggleButton';
import ResultPane from './result_pane';
import { useState } from 'react';

export default function ResultTables({data}: {data: any}) {
    const [selected, setSelected] = useState(false);
    return (
        <div className='flex flex-col'>
            {/* <ToggleButton
                value="check"
                selected={selected}
                onChange={() => {
                    setSelected(!selected);
                }}
                className='self-end bg-primary text-white hover:bg-[#0e5499] transition-colors duration-[400ms]'
                color='primary'
                >
                Compare
            </ToggleButton> */}
            {
                data.map((data: any, index: number) => (
                    <ResultPane key={index} data={data} />
                )
            )}
        </div>
    )
}
