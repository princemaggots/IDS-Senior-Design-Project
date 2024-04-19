'use client'

import Button from '@mui/material/Button';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { usePathname } from 'next/navigation'
import { columns } from '@/app/lib/data';
import { useState, useEffect } from 'react';
import { HistoryRowProps } from '@/app/lib/definitions';
import { useRouter } from 'next/navigation';

export default function HistoryTable() {
    const pathname = usePathname()
    const isPastSession = pathname === '/past_session';
    const [historyData, setHistoryData] = useState<HistoryRowProps[]>([]);
    const router = useRouter();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/db/get_history');
                const rawData = await response.json();
                const data = JSON.parse(rawData);
                const formattedData = data.map((item: any) => {
                    return {
                        id: item.pk,
                        requestTimestamp: item.fields.request_timestamp,
                        dataset: item.fields.dataset,
                        date: item.fields.request_timestamp,
                        model: item.fields.model,
                        inputJson: item.fields.input_json,
                        outputJson: item.fields.output_json,
                        precision: item.fields.stack_precision,
                        recall: item.fields.stack_recall,
                        f1: item.fields.stack_f1,
                    };
                });
                setHistoryData(formattedData);

            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
        fetchData();
    }, []);

    function handleButtonClick(row: any) {
        const model = row.model;
        router.push(`/past_session/${model}/edit_configure?output=${encodeURIComponent(row.outputJson)}&input=${encodeURIComponent(row.inputJson)}`);        
    } 

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
                <Button variant="contained" className='bg-primary' onClick={() => handleButtonClick(params.row)}>
                    Load
                </Button>
            ),
        },
    ];

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