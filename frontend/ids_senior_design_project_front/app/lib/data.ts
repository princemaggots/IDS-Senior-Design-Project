import { GridColDef } from '@mui/x-data-grid';

export const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 100 },
    { field: 'model', headerName: 'Model', width: 160 },
    { field: 'dataset', headerName: 'Dataset', width: 160 },
    { field: 'date', headerName: 'Date', width: 160 },
    { field: 'precision', headerName: 'Precision', type: 'number', width: 160 },
    { field: 'recall', headerName: 'Recall', type: 'number', width: 160 },
    { field: 'f1', headerName: 'F1 Score', type: 'number', width: 160 },
];

export const models = [
    { 
        header: 'LCCDE', 
        subHeader: 'Leader Class and Confidence Decision Ensemble', 
        description: 'an ensemble IDS, utilizing XGBoost, LightGBM, and CatBoost to select the best model for each attack class based on performance. It then uses these models and their confidence values for detection decisions.',
        href: './new_session/lccde/configure'
    },
    { 
        header: 'MTH', 
        subHeader: 'Multi-Tiered Hybrid', 
        description: 'an ensemble IDS, utilizing XGBoost, LightGBM, and CatBoost to select the best model for each attack class based on performance. It then uses these models and their confidence values for detection decisions.',
        href: './new_session/mth/configure'
    },
    { 
        header: 'Tree-based', 
        subHeader: 'Tree-based Intelligent IDS', 
        description: 'an ensemble IDS that leverages decision tree, random forest, extra trees, and XGBoost to detect intrusions in both intra-vehicle and external communication networks.',
        href: './new_session/tree_based/configure'
    }
];

export const modelToAlgorithms = {
    lccde: ['xg', 'lg', 'cb'],
    mth: ['xg', 'lg', 'cb'],
    tree_based: ['dt', 'rf', 'rt', 'xb']
};

export const algorithmFullName = {
    xg: 'XGBoost',
    lg: 'LightGBM',
    cb: 'CatBoost',
    dt: 'Decision Tree',
    rf: 'Random Forest',
    rt: 'Extra Trees',
};

export const datasetFields = {
    name: 'dataset',
    type: 'string',
    description: 'CICIDS2017 is a dataset used for cybersecurity research and analysis. It stands for "Canadian Institute for Cybersecurity Intrusion Detection Evaluation Dataset 2017." The dataset contains network traffic data captured in a simulated environment, including various types of cyber attacks and normal activities. Researchers use this dataset to develop and evaluate intrusion detection systems and other cybersecurity solutions. Car-Hacking dataset typically refers to datasets collected from experiments or simulations related to automotive cybersecurity. These datasets often include information about vulnerabilities and potential attacks on modern vehicles electronic control systems. Researchers and cybersecurity professionals use car-hacking datasets to study and address security issues in automotive systems, such as remote attacks, unauthorized access, and potential safety risks associated with vehicle connectivity and automation.',
    label: 'Select Dataset',
    defaultValue: 'CICIDS2017',
    values: ['CICIDS2017', 'Car-Hacking'],
}

export const treeBasedInputFields = [
    {
        name: 'missingVals',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Missing Values',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.2,
    },
    {
        name: 'dataRatio',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Data Ratio(Test data)',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.7,
    },
    {
        name: 'randomStateDataSplit',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Random State(Data Split)',
        min: 0,
        max: 1000,
        step: 1,
        defaultValue: 42,
    },
    {
        name: 'samplingStrat',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Sampling Strategy',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.3,
    },
    {
        name: 'randomStateDT',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Random State(Decision Tree)',
        min: 0,
        max: 1000,
        step: 1,
        defaultValue: 42,
    },
    {
        name: 'randomStateRF',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Random State(Random Forest)',
        min: 0,
        max: 1000,
        step: 1,
        defaultValue: 42,
    },
    {
        name: 'randomStateET',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Random Strategy(Extra Tree)',
        min: 0,
        max: 1000,
        step: 1,
        defaultValue: 42,
    },
    {
        name: 'nEst',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'n-Estimator',
        min: 1,
        max: 1000,
        step: 1,
        defaultValue: 100,
    },
    {
        name: 'threshold',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Feature Threshold',
        min: 0,
        max: 1,
        step: 0.01,
        defaultValue: 0.5,
    },
];

export const mthInputFields = [
    {
        name: 'fcbfk',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'FCBF-K',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.5,
    },
    {
        name: 'dataRatio',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Data Ratio(Test data)',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.7,
    },
    {
        name: 'samplingStrat2',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Sampling Strategy(class 2)',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.3,
    },
    {   
        name: 'samplingStrat4',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Sampling Strategy(class 4)',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.5,
    },
    {
        name: 'nEstXGB1',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'n-Esimator(XGBoost 1)',
        min: 1,
        max: 1000,
        step: 1,
        defaultValue: 100,
    },
    {
        name: 'nEstXGB2',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'n-Esimator(XGBoost 2)',
        min: 1,
        max: 1000,
        step: 1,
        defaultValue: 200,
    },
    {
        name: 'nEstXGB3',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'n-Esimator(XGBoost 3)',
        min: 1,
        max: 1000,
        step: 1,
        defaultValue: 300,
    },
    {
        name: 'nEstRF',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'n-Esimator(Random Forest)',
        min: 1,
        max: 1000,
        step: 1,
        defaultValue: 400,
    },
    {
        name: 'nEstET',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'n-Esimator(Extra Tree)',
        min: 1,
        max: 1000,
        step: 1,
        defaultValue: 500,
    },
    {
        name: 'threshold',
        description: 'Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  Description  ',
        label: 'Feature Threshold',
        min: 0,
        max: 1,
        step: 0.01,
        defaultValue: 0.5,
    },
];

export const lccdeInputFields = [
    {
        name: 'test_size',
        type: 'number',
        description: 'The proportion of the dataset to include in the test split.',
        label: 'Test Data Size',
        min: 0,
        max: 1,
        step: 0.1,
        defaultValue: 0.2,
    },
    {
        name: "random_state",
        type: 'number',
        description: "Controls the randomness of the dataset split.",
        label: "Random State",
        min: 0,
        max: 41,
        step: 1,
        defaultValue: 0
    },
    {
        name: "sampling_strat2",
        type: 'number',
        description: "The size of the second sampling strategy.",
        label: "Sampling Strategy 2",
        min: 100,
        max: 5000,
        step: 10,
        defaultValue: 1000
    },
    {
        name: "sampling_strat4",
        type: 'number',
        description: "The size of the fourth sampling strategy.",
        label: "Sampling Strategy 4",
        min: 100,
        max: 5000,
        step: 10,
        defaultValue: 1000
    },
    {
        name: "xg_eta",
        type: 'number',
        description: "Step size shrinkage used in update to prevent overfitting in XGBoost.",
        label: "XGBoost Eta",
        min: 0.1,
        max: 1.0,
        step: 0.1,
        defaultValue: 0.3
    },
    {
        name: "xg_max_depth",
        type: 'number',
        description: "Maximum depth of a tree in XGBoost.",
        label: "XGBoost Max Depth",
        min: 1,
        max: 50,
        step: 1,
        defaultValue: 6
    },
    {
        name: "xg_subsample",
        type: 'number',
        description: "Subsample ratio of the training instances in XGBoost.",
        label: "XGBoost Subsample",
        min: 1,
        max: 10,
        step: 1,
        defaultValue: 1
    },
    {
        name: "xg_lambda",
        type: 'number',
        description: "L2 regularization term on weights in XGBoost.",
        label: "XGBoost Lambda",
        min: 1,
        max: 10,
        step: 1,
        defaultValue: 1
    },
    {
        name: "xg_alpha",
        type: 'number',
        description: "L1 regularization term on weights in XGBoost.",
        label: "XGBoost Alpha",
        min: 0,
        max: 10,
        step: 1,
        defaultValue: 0
    },
    {
        name: "xg_gamma",
        type: 'number',
        description: "Minimum loss reduction required to make a further partition on a leaf node of the tree in XGBoost.",
        label: "XGBoost Gamma",
        min: 0,
        max: 10,
        step: 1,
        defaultValue: 0
    },
    {
        name: "xg_colsample_bytree",
        type: 'number',
        description: "Subsample ratio of columns when constructing each tree in XGBoost.",
        label: "XGBoost Colsample by Tree",
        min: 1,
        max: 10,
        step: 1,
        defaultValue: 1
    },
    {
        name: "xg_min_child_weight",
        type: 'number',
        description: "Minimum sum of instance weight (hessian) needed in a child in XGBoost.",
        label: "XGBoost Min Child Weight",
        min: 1,
        max: 10,
        step: 1,
        defaultValue: 1
    },
    {
        name: "xg_n_estimators",
        type: 'number',
        description: "Number of boosting rounds in XGBoost.",
        label: "XGBoost Number of Estimators",
        min: 1,
        max: 10,
        step: 1,
        defaultValue: 1
    },
    {
        name: "cb_iterations",
        type: 'number',
        description: "The number of boosting iterations for CatBoost.",
        label: "CatBoost Iterations",
        min: 10,
        max: 1500,
        step: 10,
        defaultValue: 1000
    },
    {
        name: "cb_learning_rate",
        type: 'number',
        description: "The learning rate for CatBoost.",
        label: "CatBoost Learning Rate",
        min: 0.01,
        max: 0.1,
        step: 0.01,
        defaultValue: 0.03
    },
    {
        name: "cb_depth",
        type: 'number',
        description: "The depth of the trees for CatBoost.",
        label: "CatBoost Depth",
        min: 1,
        max: 30,
        step: 1,
        defaultValue: 6
    },
    {
        name: "cb_random_state",
        type: 'number',
        description: "Controls the randomness of the CatBoost algorithm.",
        label: "CatBoost Random State",
        min: 0,
        max: 41,
        step: 1,
        defaultValue: 0
    },
    {
        name: "cb_loss_function",
        type: 'string',
        description: "The loss function for CatBoost.",
        label: "CatBoost Loss Function",
        defaultValue: "MultiClass",
        values: ["MultiClass"]
    },
    {
        name: "lg_boosting",
        type: 'string',
        description: "The boosting type for LightGBM.",
        label: "LightGBM Boosting",
        defaultValue: "gbdt",
        values: ["gbdt"]
    },
    {
        name: "lg_learning_rate",
        type: 'number',
        description: "The learning rate for LightGBM.",
        label: "LightGBM Learning Rate",
        min: 0.1,
        max: 1.0,
        step: 0.1,
        defaultValue: 0.1
    },
    {
        name: "lg_lambda_l1",
        type: 'number',
        description: "L1 regularization term on weights for LightGBM.",
        label: "LightGBM Lambda L1",
        min: 0,
        max: 10,
        step: 1,
        defaultValue: 0
    },
    {
        name: "lg_num_leaves",
        type: 'number',
        description: "Maximum tree leaves for LightGBM.",
        label: "LightGBM Number of Leaves",
        min: 1,
        max: 100,
        step: 1,
        defaultValue: 31
    },
    {
        name: "lg_num_iterations",
        type: 'number',
        description: "The number of boosting iterations for LightGBM.",
        label: "LightGBM Number of Iterations",
        min: 1,
        max: 150,
        step: 1,
        defaultValue: 100
    },
    {
        name: "lg_max_depth",
        type: 'number',
        description: "Maximum depth of the tree model for LightGBM. Negative value means no limit.",
        label: "LightGBM Max Depth",
        min: -10,
        max: 10,
        step: 1,
        defaultValue: -1
    }
];