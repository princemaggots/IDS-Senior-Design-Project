'use client'

import HistoryTable from './components/history_table';
import Button from '@mui/material/Button';
import { Suspense } from 'react';

export default function Home() {
  

  return (
    <div className='flex flex-col justify-center'>
      <p className='text-xl mb-4'> <strong>Home</strong></p>
      <div className='flex justify-around mb-10 '>
        <Button variant="contained" href="./new_session">Start a new session</Button>
        <Button variant="contained" href='./past_session'>Load a past session</Button>
      </div>
      <Suspense fallback={<p>Loading execution history...</p>}>
        <p className='text-gray-400 text-xs'>*Hover over each table header cell to sort the records</p>
        <HistoryTable />
      </Suspense>
    </div>
  );
}
