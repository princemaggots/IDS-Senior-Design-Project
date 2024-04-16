// row data for history table in the landing page
export const rows = [
    { id: 1, model: 'LCCDE', dataset: 'CICIDS2017', date: 'April 2, 2024', precision: 0.9, recall: 0.8, f1: 0.85 },
    { id: 2, model: 'Three based', dataset: 'Car-Hacking', date: 'April 15, 2024', precision: 1.0, recall: 0.8, f1: 0.83 },
    { id: 3, model: 'MTH', dataset: 'CICIDS2017', date: 'April 20, 2024', precision: 0.9, recall: 1.0, f1: 0.75 },
    { id: 4, model: 'LCCDE', dataset: 'Car-Hacking', date: 'April 27, 2024', precision: 1.0, recall: 0.8, f1: 0.82 },
    { id: 5, model: 'Three based', dataset: 'CICIDS2017', date: 'May 5, 2024', precision: 1.0, recall: 1.0, f1: 0.93 },
    { id: 6, model: 'MTH', dataset: 'CICIDS2017', date: 'May 12, 2024', precision: 0.9, recall: 0.8, f1: 0.96 },
    { id: 7, model: 'LCCDE', dataset: 'Car-Hacking', date: 'May 21, 2024', precision: 0.9, recall: 1.0, f1: 0.90 },
    { id: 8, model: 'Three based', dataset: 'CICIDS2017', date: 'May 29, 2024', precision: 0.9, recall: 0.8, f1: 0.98 },
    { id: 9, model: 'LCCDE', dataset: 'CICIDS2017', date: 'June 1, 2024', precision: 1.0, recall: 1.0, f1: 0.975 },
    { id: 10, model: 'MTH', dataset: 'Car-Hacking', date: 'June 6, 2024', precision: 1.0, recall: 0.8, f1: 0.95 },
    { id: 11, model: 'MTH', dataset: 'Car-Hacking', date: 'June 17, 2024', precision: 0.9, recall: 0.8, f1: 0.75 },
];

export const ResultTableRows = [
    {attackClass:'0 BENIGN', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
    {attackClass:'1 Bot', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
    {attackClass:'2 Brute Force', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
    {attackClass:'3 DoS', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
    {attackClass:'4 Infiltration', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
    {attackClass:'5 PortScan', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
    {attackClass:'6 WebAttack', precision: 1.0, recall: 1.0, f1: 1.0, support: 3656},
];

export const ModelSubResultTableRows = [
    {evaluationMatrix: 'Accuracy', value: 0.997014},
    {evaluationMatrix: 'Precision', value: 0.997023},
    {evaluationMatrix: 'Recall', value: 0.997014},
    {evaluationMatrix: 'Average of F1', value: 0.996987},
];

export const ClassSubResultTableRows = [
    {attackClass: '0 BENIGN', value: 0.997950},
    {attackClass: '1 Bot', value: 0.997543},
    {attackClass: '2 Brute Force', value: 0.997950},
    {attackClass: '3 DoS', value: 0.990920},
    {attackClass: '4 Infiltration', value: 0.997782},
    {attackClass: '5 PortScan', value: 0.993548},
    {attackClass: '6 WebAttack', value: 1.0},
];

export const OutputData = {
    "lg_class_f1": [
        0.9982238010657194,
        0.993514915693904,
        1.0,
        0.9975429975429976,
        0.8571428571428571,
        0.9935483870967742,
        0.9977827050997783
    ],
    "lg_class_report": "              precision    recall  f1-score   support\n\n           0       1.00      1.00      1.00      3656\n           1       1.00      0.99      0.99       387\n           2       1.00      1.00      1.00        14\n           3       1.00      1.00      1.00       612\n           4       1.00      0.75      0.86         8\n           5       0.99      1.00      0.99       231\n           6       1.00      1.00      1.00       452\n\n    accuracy                           1.00      5360\n   macro avg       1.00      0.96      0.98      5360\nweighted avg       1.00      1.00      1.00      5360\n",
    "lg_acc_score": 0.9973880597014926,
    "lg_prec_score": 0.9973973431077559,
    "lg_rec_score": 0.9973880597014926,
    "lg_f1": 0.9973614564454708,
    "lg_confusion_matrix": [
        [
            3653,
            0,
            0,
            0,
            0,
            3,
            0
        ],
        [
            4,
            383,
            0,
            0,
            0,
            0,
            0
        ],
        [
            0,
            0,
            14,
            0,
            0,
            0,
            0
        ],
        [
            3,
            0,
            0,
            609,
            0,
            0,
            0
        ],
        [
            1,
            1,
            0,
            0,
            6,
            0,
            0
        ],
        [
            0,
            0,
            0,
            0,
            0,
            231,
            0
        ],
        [
            2,
            0,
            0,
            0,
            0,
            0,
            450
        ]
    ],
    "xb_class_f1": [
        0.9857084524295631,
        0.9573333333333334,
        0.9655172413793104,
        0.9698942229454841,
        0.6153846153846154,
        0.9892008639308856,
        0.9606299212598425
    ],
    "xb_class_report": "              precision    recall  f1-score   support\n\n           0       0.98      0.99      0.99      3656\n           1       0.99      0.93      0.96       387\n           2       0.93      1.00      0.97        14\n           3       0.97      0.97      0.97       612\n           4       0.80      0.50      0.62         8\n           5       0.99      0.99      0.99       231\n           6       0.98      0.94      0.96       452\n\n    accuracy                           0.98      5360\n   macro avg       0.95      0.90      0.92      5360\nweighted avg       0.98      0.98      0.98      5360\n",
    "xb_acc_score": 0.9794776119402985,
    "xb_prec_score": 0.9794227314364907,
    "xb_rec_score": 0.9794776119402985,
    "xb_f1": 0.979284292687498,
    "xb_confusion_matrix": [
        [
            3621,
            3,
            1,
            19,
            1,
            3,
            8
        ],
        [
            28,
            359,
            0,
            0,
            0,
            0,
            0
        ],
        [
            0,
            0,
            14,
            0,
            0,
            0,
            0
        ],
        [
            16,
            0,
            0,
            596,
            0,
            0,
            0
        ],
        [
            2,
            1,
            0,
            1,
            4,
            0,
            0
        ],
        [
            0,
            0,
            0,
            0,
            0,
            229,
            2
        ],
        [
            24,
            0,
            0,
            1,
            0,
            0,
            427
        ]
    ],
    "cb_class_f1": [
        0.9963059242030373,
        0.9909677419354839,
        0.9655172413793104,
        0.991869918699187,
        0.7692307692307693,
        0.9892008639308856,
        0.9922308546059934
    ],
    "cb_class_report": "              precision    recall  f1-score   support\n\n           0       1.00      1.00      1.00      3656\n           1       0.99      0.99      0.99       387\n           2       0.93      1.00      0.97        14\n           3       0.99      1.00      0.99       612\n           4       1.00      0.62      0.77         8\n           5       0.99      0.99      0.99       231\n           6       1.00      0.99      0.99       452\n\n    accuracy                           0.99      5360\n   macro avg       0.98      0.94      0.96      5360\nweighted avg       0.99      0.99      0.99      5360\n",
    "cb_acc_score": 0.9944029850746269,
    "cb_prec_score": 0.9944299177126288,
    "cb_rec_score": 0.9944029850746269,
    "cb_f1": 0.9943448131795408,
    "cb_confusion_matrix": [
        [
            3641,
            3,
            0,
            7,
            0,
            3,
            2
        ],
        [
            3,
            384,
            0,
            0,
            0,
            0,
            0
        ],
        [
            0,
            0,
            14,
            0,
            0,
            0,
            0
        ],
        [
            2,
            0,
            0,
            610,
            0,
            0,
            0
        ],
        [
            2,
            1,
            0,
            0,
            5,
            0,
            0
        ],
        [
            2,
            0,
            0,
            0,
            0,
            229,
            0
        ],
        [
            3,
            0,
            1,
            1,
            0,
            0,
            447
        ]
    ],
    "lccde_class_f1": [
        0.9982238010657194,
        0.993514915693904,
        1.0,
        0.9975429975429976,
        0.8571428571428571,
        0.9935483870967742,
        0.9977827050997783
    ],
    "lccde_acc_score": 0.9973880597014926,
    "lccde_prec_score": 0.9973973431077559,
    "lccde_rec_score": 0.9973880597014926,
    "lccde_f1": 0.9973614564454708
};