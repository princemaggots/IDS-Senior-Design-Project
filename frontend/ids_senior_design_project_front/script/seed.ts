import { GridColDef } from '@mui/x-data-grid';

// column data for history table in the landing page
export const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 100 },
    { field: 'algorithm', headerName: 'Algorithm', width: 200 },
    { field: 'dataset', headerName: 'Dataset', width: 200 },
    { field: 'date', headerName: 'Date', width: 200 },
    { field: 'precision', headerName: 'Precision', type: 'number', width: 100 },
    { field: 'recall', headerName: 'Recall', type: 'number', width: 160 },
    { field: 'f1', headerName: 'F1 Score', type: 'number', width: 160 },
];

// row data for history table in the landing page
export const rows = [
    { id: 1, algorithm: 'LCCDE', dataset: 'CICIDS2017', date: 'April 2, 2024', precision: 0.9, recall: 0.8, f1: 0.85 },
    { id: 2, algorithm: 'Three based', dataset: 'Car-Hacking', date: 'April 15, 2024', precision: 1.0, recall: 0.8, f1: 0.83 },
    { id: 3, algorithm: 'MTH', dataset: 'CICIDS2017', date: 'April 20, 2024', precision: 0.9, recall: 1.0, f1: 0.75 },
    { id: 4, algorithm: 'LCCDE', dataset: 'Car-Hacking', date: 'April 27, 2024', precision: 1.0, recall: 0.8, f1: 0.82 },
    { id: 5, algorithm: 'Three based', dataset: 'CICIDS2017', date: 'May 5, 2024', precision: 1.0, recall: 1.0, f1: 0.93 },
    { id: 6, algorithm: 'MTH', dataset: 'CICIDS2017', date: 'May 12, 2024', precision: 0.9, recall: 0.8, f1: 0.96 },
    { id: 7, algorithm: 'LCCDE', dataset: 'Car-Hacking', date: 'May 21, 2024', precision: 0.9, recall: 1.0, f1: 0.90 },
    { id: 8, algorithm: 'Three based', dataset: 'CICIDS2017', date: 'May 29, 2024', precision: 0.9, recall: 0.8, f1: 0.98 },
    { id: 9, algorithm: 'LCCDE', dataset: 'CICIDS2017', date: 'June 1, 2024', precision: 1.0, recall: 1.0, f1: 0.975 },
    { id: 10, algorithm: 'MTH', dataset: 'Car-Hacking', date: 'June 6, 2024', precision: 1.0, recall: 0.8, f1: 0.95 },
    { id: 11, algorithm: 'MTH', dataset: 'Car-Hacking', date: 'June 17, 2024', precision: 0.9, recall: 0.8, f1: 0.75 },
];