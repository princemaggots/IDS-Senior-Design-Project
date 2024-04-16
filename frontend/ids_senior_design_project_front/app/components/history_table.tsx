'use client'

import Button from '@mui/material/Button';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { rows } from '@/script/seed';
import { usePathname } from 'next/navigation'
import { columns } from '@/app/lib/data';
import { useState, useEffect } from 'react';
import { HistoryRowProps } from '@/app/lib/definitions';


export default function HistoryTable() {
    const pathname = usePathname()
    const isPastSession = pathname === '/past_session';

    const [historyData, setHistoryData] = useState<HistoryRowProps[]>([]);

    useEffect(() => {
        // fetch('https://66157f68b8b8e32ffc7b1be3.mockapi.io/api/records')
        fetch('http://127.0.0.1:8000/db/get_history')
        .then(response => response.json())
        .then(data => setHistoryData(data))
        .catch(error => console.error('Error fetching data:', error));
    }, []);

    const columnsWithButton: GridColDef[] = [
        ...columns,
        {
            field: 'load-btn',
            headerName: '',
            width: 160,
            sortable: false,
            align: 'center',
            disableColumnMenu: true,
            renderCell: (params) => (
                <Button variant="contained" className='bg-primary'onClick={() => handleButtonClick(params.row)}>
                    Load
                </Button>
            ),
        },
    ];
    
    function handleButtonClick(row: any) {
        console.log(row)
    }
    // replace 'historyData' with 'rows' to test with seed data
    return (
        <div className='w-full h-[371px] flex justify-center'>
            <DataGrid
                rows={historyData} 
                columns={isPastSession ? columnsWithButton : columns}
                disableRowSelectionOnClick
                pageSizeOptions={[5, 10, 20]}
                initialState={{
                    pagination: {
                        paginationModel: { page: 0, pageSize: 5 },
                    },
                }}
            />
        </div>
    )
};