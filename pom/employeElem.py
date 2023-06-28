class employee():
    # add
    menuPim = "//a[@href='/web/index.php/pim/viewPimModule']/span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"
    btnAddEmp = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    inputAddFirstName = "//input[@name='firstName']"
    inputAddMiddleName = "//input[@name='middleName']"
    inputAddLastName = "//input[@name='lastName']"
    btnSaveAdd = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    expAddEmp = "//h6[.='Personal Details']"
    btnCancelAdd = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    errMsgFirstName = "//div[@class='--name-grouped-field']/div[1]/span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    errMsgMiddleName = ""
    errMsgLastName = "//div[@class='--name-grouped-field']/div[3]/span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    inputEmpId = "//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input[@class='oxd-input oxd-input--active']"
    errMsgEmpId = "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"

    #edit
    btnEdit = "//div[@class='oxd-table-body oxd-card-table-body']/div[1]//button[2]"
    btnSaveEdit = "//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    toasterSuccess = ".oxd-toast-container"
    btnDelete = "//div[@class='oxd-table-body oxd-card-table-body']/div[1]//button[1]"
    modalDelYes = ".oxd-button--label-danger"
