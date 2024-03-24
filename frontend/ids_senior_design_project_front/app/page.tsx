import * as React from 'react';
import HistoryTable from './components/history_table';
import Button from '@mui/material/Button';

export default function Home() {
  return (
    <div className='flex flex-col justify-center'>
      <div className='flex justify-around'>
        <Button variant="contained" href="./new_session">Start a new session</Button>
        <Button variant="contained" href='./past_session'>Load a past session</Button>
      </div>
      <div className='mt-10 w-full h-full flex justify-center'>
        <HistoryTable />
      </div>
    </div>
  );
}
